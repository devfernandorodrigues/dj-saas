from django.shortcuts import redirect
from django.urls import reverse


def subscription_required(function):
    def wrapper(request, *args, **kw):
        user = request.user
        if (
            not user.customer
            or not user.customer.has_any_active_subscription()
        ):
            return redirect(reverse("core:plans"))
        return function(request, *args, **kw)

    return wrapper
