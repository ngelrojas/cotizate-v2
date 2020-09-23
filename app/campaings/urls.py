from django.urls import path
from .header.views import CampaingHeader
from .body.views import CampaingBody

app_name = "campaing-app"

urlpatterns = [
    path(
        "campaing-header",
        CampaingHeader.as_view({"get": "list", "post": "create"}),
        name="campaing-header",
    ),
    path(
        "campaing-header/<int:pk>",
        CampaingHeader.as_view(
            {"get": "retrieve", "put": "update", "delete": "delete"}
        ),
        name="campaing-header-detail",
    ),
    path(
        "campaing-body", CampaingBody.as_view({"post": "create"}), name="campaing-body"
    ),
    path(
        "campaing-body/<int:pk>",
        CampaingBody.as_view({"get": "retrieve", "put": "update", "delete": "delete"}),
        name="campaing-body-detail",
    ),
]
