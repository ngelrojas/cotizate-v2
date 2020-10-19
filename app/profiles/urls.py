from django.urls import path
from profiles.personal import PersonalProfileView


app_name = "profile"

urlpatterns = [
    path(
        "profile/personal",
        PersonalProfileView.as_view({"post": "create"}),
        name="personal",
    ),
    path(
        "profile/personal/<int:pk>",
        PersonalProfileView.as_view({"get": "retrieve", "put": "update"}),
        name="personal-detail",
    ),
]
