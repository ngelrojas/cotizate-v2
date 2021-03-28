from django.urls import path
from updatings import views
from updatings import public

app_name = "updating"

urlpatterns = [
    path("updatings", views.UpdatingView.as_view({"post": "create"}), name="updatings"),
    path(
        "updatings/<int:pk>",
        views.UpdatingView.as_view({"put": "update", "get": "retrieve"}),
        name="upldating-details",
    ),
    path(
        "alterations/<int:pk>",
        public.UpdatingPublicView.as_view({"get": "retrieve"}),
        name="upldating-alterations-details",
    ),
]
