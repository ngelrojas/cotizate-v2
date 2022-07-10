from django.urls import path
from .views import CamapingView

app_name = "campaing"

urlpatterns = [
    path(
        "user/campaing",
        CampaingView.as_view({"get": "list", "post": "create"}),
        name="campaing",
    ),
    path(
        "user/campaing/<int:pk>",
        CampaingView.as_view(
            {"get": "retrieve", "put": "update", "delete": "delete"}
        ),
        name="campaing-detail",
    ),
]
