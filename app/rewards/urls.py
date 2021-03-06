from django.urls import path
from .views import RewardView, RewardrView

app_name = "reward"

urlpatterns = [
    path("reward", RewardView.as_view({"post": "create"}), name="reward"),
    path(
        "reward/<int:pk>",
        RewardView.as_view({"get": "retrieve", "put": "update", "delete": "delete"}),
        name="reward-detail",
    ),
    path(
        "rewardr/<int:pk>",
        RewardrView.as_view({"get": "retrieve"}),
        name="reward-detail-each",
    ),
]
