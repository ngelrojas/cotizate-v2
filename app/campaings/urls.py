from django.urls import path
from .views import CampaingView 
from .views import CampaingItems
from .views import CampaingStatus

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
    path("user/campaing/<int:pk>/category",
        CampaingItems.as_view({"get": "list"}),
        name="campaing-category"
    ),
    path("user/campaing/<int:pk>/city",
        CampaingItems.as_view({"get": "retrieve"}),
        name="campaing-city"
    ),
    path("user/campaing/<str:pk>/status",
        CampaingStatus.as_view({"get": "list"}),
        name="campaing-status"
    ),
    path("user/campaing/<str:pk>/flag",
        CampaingStatus.as_view({"get": "retrieve"}),
        name="campaing-flag"
    ),
]
