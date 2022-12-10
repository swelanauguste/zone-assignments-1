from django.urls import path

from . import views

app_name = "zones"

urlpatterns = [
    path("", views.ZoneListView.as_view(), name="zone-list"),
    path("detail/<int:pk>/", views.ZoneDetailView.as_view(), name="zone-detail"),
]
