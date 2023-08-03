from core import views
from django.urls import path

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("plans/", views.plans, name="plans"),
    path("subscription/", views.subscription, name="subscription"),
    path("stripe/cancel/", views.cancel, name="stripe_cancel"),
    path("stripe/success/", views.success, name="stripe_success"),
    path("app/dashboard/", views.dashboard, name="dashboard"),
    path("app/profile/", views.profile, name="profile"),
    path(
        "app/subscription/cancel/",
        views.subscription_cancel,
        name="subscription_cancel",
    ),
]
