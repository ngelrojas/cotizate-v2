from django.urls import path
from profiles.personal import UpdatePersonalView
from profiles.company import UpdateCompanyView

app_name = "profile"

urlpatterns = [
    path(
        "personal/profile/<int:pk>",
        UpdatePersonalView.as_view({"get": "retrieve", "put": "update"}),
        name="personal",
    ),
    path(
        "company/profile",
        UpdateCompanyView.as_view({"get": "list", "post": "create"}),
        name="company",
    ),
    path(
        "company/profile/<int:pk>",
        UpdateCompanyView.as_view(
            {"get": "retrieve", "put": "update", "delete": "delete"}
        ),
        name="company-detail",
    ),
]
