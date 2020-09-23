from django.urls import path
from .networkPA import SnetWPAView
from .networkPP import SnetWPPView
from .networkPC import SnetWPCView

app_name = "social-networks"

urlpatterns = [
    path(
        "social-network-pa",
        SnetWPAView.as_view({"get": "list", "post": "create"}),
        name="social-network-pa-list",
    ),
    path(
        "social-network-pa/<pk:int>",
        SnetWPAView.as_view({"get": "retrieve", "put": "update", "delete": "delete"}),
        name="social-network-pa-details",
    ),
    path(
        "social-network-pp",
        SnetWPPView.as_view({"get": "list", "post": "create"}),
        name="social-network-pp-list",
    ),
    path(
        "social-network-pp/<pk:int>",
        SnetWPPView.as_view({"get": "retrieve", "put": "update", "delete": "delete"}),
        name="social-network-pp-details",
    ),
    path(
        "social-network-pc",
        SnetWPCView.as_view({"get": "list", "post": "create"}),
        name="social-network-pc-list",
    ),
    path(
        "social-network-pc/<pk:int>",
        SnetWPCView.as_view({"get": "retrieve", "put": "update", "delete": "delete"}),
        name="social-network-pc-details",
    ),
]
