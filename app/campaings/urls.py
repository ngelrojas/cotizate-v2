from django.urls import path
from .header.views import CampaingsHeader
from .header.helpers import HelperHeader
from .body.views import CampaingsBody

app_name = "campaing-app"

urlpatterns = [
    path(
        "campaing-header",
        CampaingsHeader.as_view({"get": "list", "post": "create"}),
        name="campaing-header",
    ),
    path(
        "campaing-header/<int:pk>",
        CampaingsHeader.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="campaing-header-detail",
    ),
    path(
        "campaing-body", CampaingsBody.as_view({"post": "create"}), name="campaing-body"
    ),
    path(
        "campaing-body/<int:pk>",
        CampaingsBody.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="campaing-body-detail",
    ),
    path(
        "campaing-header-last",
        HelperHeader.as_view({"get": "list"}),
        name="campaing-last",
    ),
]
