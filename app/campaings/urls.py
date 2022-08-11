from django.urls import path
from .views import CampaingView 
from .views import CampaingItems
from .views import CampaingStatus
from .views import CampaingStuff
from .views import CampaingDates
from .campaing_views import CampaingView1
from .campaing_views import CampaingView2
from .campaing_views import CampaingView3
from .campaing_views import CampaingView4
from .campaing_views import CampaingView5
from .campaing_views import CampaingView6

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
    path("campaing/all", CampaingView1.as_view({"get": "list"}),
        name="public-campaing-all"
    ),
    path("campaing/<int:pk>/category",
        CampaingView1.as_view({"get": "retrieve"}),
        name="public-campaing-category"
    ),
    path("campaing/<int:pk>/city",
        CampaingView2.as_view({"get": "list"}),
        name="public-campaing-city"
    ),
    path("campaing/title/<str:title>",
        CampaingView2.as_view({"get": "retrieve"}),
        name="public-campaing-title"
    ),
    path("campaing/<int:flag>/flag",
        CampaingView3.as_view({"get": "list"}),
        name="public-campaing-flag"
    ),
    path("campaing/<int:role>/role",
        CampaingView3.as_view({"get": "retrieve"}),
        name="public-campaing-role"
    ),
    path("campaing/created/<str:dinit>/<str:dfinal>",
        CampaingView4.as_view({"get": "list"}),
        name="public-campaing-created"
    ),
    path("campaing/ended/<str:dinit>/<str:dfinal>",
        CampaingView4.as_view({"get": "retrieve"}),
        name="public-campaing-ended"
    ),
    path("campaing/status/<int:field_status>/<int:flag>/flag",
        CampaingView5.as_view({"get": "list"}),
        name="public-campaing-status-flag"
    ),
    path("campaing/exact-title/<str:title>",
        CampaingView5.as_view({"get": "retrieve"}),
        name="public-campaing-exact-title"
    ),
    path("campaing/<int:campaing_id>",
        CampaingView6.as_view({"get": "retrieve"}),
        name="public-campaing-id"
    ),
]
