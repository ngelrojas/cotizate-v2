from django.urls import path
from .association import AssociationView


app_name = "profile-association"

urlpatterns = [
    path(
        "profile/association",
        AssociationView.as_view({"post": "create"}),
        name="association",
    ),
    path(
        "profile/association/<int:pk>",
        AssociationView.as_view(
            {"get": "retrieve", "put": "update", "delete": "delete"}
        ),
        name="association-detail",
    ),
]
