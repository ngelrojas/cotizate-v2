from django.urls import path
from .views import FollowerView

app_name = "follow"

urlpatterns = [
    path("followers", FollowerView.as_view({"post": "create"}), name="followers"),
    path(
        "followers/<int:pk>/<int:follow>",
        FollowerView.as_view({"get": "retrieve", "put": "update"}),
        name="detail-follow",
    ),
]
