from django.urls import path
from .views import ImproveView

app_name = "improve"

urlpatterns = [
    path(
        "improve",
        ImproveView.as_view({"get": "list", "post": "create"}),
        name="improve",
    ),
    path(
        "improve/<int:pk>",
        ImproveView.as_view({"get": "retrieve", "put": "update", "delete": "delete"}),
        name="improve-detail",
    ),
]
