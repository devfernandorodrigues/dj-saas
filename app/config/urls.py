from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("stripe/", include("djstripe.urls", namespace="djstripe")),
    path("__reload__/", include("django_browser_reload.urls")),
]
