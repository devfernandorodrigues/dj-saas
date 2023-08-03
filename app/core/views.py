import stripe
from core.decorators import subscription_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from djstripe import settings as djstripe_settings
from djstripe.enums import SubscriptionStatus
from djstripe.models import Customer, Price, Product, Subscription

stripe.api_key = djstripe_settings.djstripe_settings.STRIPE_SECRET_KEY


def home(request):
    return render(request, "index.html")


@login_required
def plans(request):
    user = request.user
    customer, _ = Customer.get_or_create(user)

    if not user.customer:
        user.customer = customer
        user.save()

    if customer.has_any_active_subscription():
        return redirect("core:dashboard")

    products = Product.objects.filter(active=True)

    return render(
        request, "plans.html", {"products": products, "customer": customer}
    )


@login_required
def subscription(request):
    if request.method == "GET":
        return redirect("core:plans")

    if request.method == "POST":
        price = get_object_or_404(Price, id=request.POST.get("price"))

        customer_key = (
            djstripe_settings.djstripe_settings.SUBSCRIBER_CUSTOMER_KEY
        )
        metadata = {
            f"{customer_key}": request.user.id,
        }

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            customer=request.user.customer.id,
            line_items=[
                {
                    "price": price.id,
                    "quantity": 1,
                }
            ],
            payment_method_collection="if_required",
            mode="subscription",
            success_url=request.build_absolute_uri("/stripe/success/"),
            cancel_url=request.build_absolute_uri("/stripe/cancel/"),
            metadata=metadata,
        )

        return render(
            request,
            "checkout.html",
            {
                "CHECKOUT_SESSION_ID": session.id,
                "STRIPE_PUBLIC_KEY": (
                    djstripe_settings.djstripe_settings.STRIPE_PUBLIC_KEY
                ),
            },
        )


@login_required
@subscription_required
def dashboard(request):
    subscriptions = request.user.customer.subscriptions.filter(
        status=SubscriptionStatus.active
    )
    return render(
        request, "app/dashboard.html", {"subscriptions": subscriptions}
    )


@login_required
@subscription_required
def profile(request):
    return render(request, "app/profile.html")


@login_required
def success(request):
    return render(request, "success.html")


@login_required
def cancel(request):
    return render(request, "cancel.html")


def subscription_cancel(request):
    Subscription.cancel(request.user.customer.subscription)
    return redirect("core:plans")
