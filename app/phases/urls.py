from django.urls import path
from .views import PhaseView
from .views import PhaseListView

app_name = "phase"

urlpatterns = [
    path("phase", PhaseView.as_view({"post": "create"}), name="phase"),
    path(
        "phase/<int:pk>/<int:cp>",
        PhaseView.as_view({"get": "retrieve", "put": "update", "delete": "delete"}),
        name="phase-detail",
    ),
    path(
        "phases/<int:pk>",
        PhaseView.as_view({"get": "list"}),
        name="phase-list",
    ),
]
