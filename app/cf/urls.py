from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("zones.urls", namespace="zones")),
    path("admin/", admin.site.urls),
]
