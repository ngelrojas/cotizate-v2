from django.urls import path
from profiles.personal import PersonalProfileView


app_name = "profile"

urlpatterns = [
    path(
        "user/profile/personal",
        PersonalProfileView.as_view(
            {"get": "list", "post": "create"}
        ),
        name="personal",
    ),
    path(
        "user/profile/personal/<int:pk>",
        PersonalProfileView.as_view(
            {"get": "retrieve", "put": "update", "delete": "delete"}
        ),
        name="personal-detail",
    ),
]
