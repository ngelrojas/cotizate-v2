from django.urls import path
from .views import CampaingView 
from .views import CampaingItems
from .views import CampaingStatus
from .views import CampaingStuff
from .views import CampaingDates

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
    path("user/campaing/<int:pk>/<int:fl>", 
        CampaingStuff.as_view({"get": "list"}),
        name="campaing-status-flag"
    ),
    path("user/campaing/<int:pk>/role",
        CampaingStuff.as_view({"get": "retrieve"}),
        name="campaing-role"
    ),
    path("user/campaing/created/<str:dipk>/<str:dfpk>",
        CampaingDates.as_view({"get": "list"}),
        name="campaing-created"
    ),
    path("user/campaing/ended/<str:dipk>/<str:dfpk>",
        CampaingDates.as_view({"get": "retrieve"}),
        name="campaing-ended"
    ),
]
