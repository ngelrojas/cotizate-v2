from django.urls import path
from .views import PhaseView

app_name = "phase"

urlpatterns = [
    path("phase", PhaseView.as_view({"get": "list", "post": "create"}), name="phase"),
    path(
        "phase/<int:pk>",
        PhaseView.as_view({"get": "retrieve", "put": "update", "delete": "delete"}),
        name="phase-detail",
    ),
]
