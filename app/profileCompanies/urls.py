from django.urls import path
from .company import CompanyView


app_name = "company"

urlpatterns = [
    path(
        "user/profile/company",
        CompanyView.as_view({"get": "list", "post": "create"}),
        name="profile",
    ),
    path(
        "user/profile/company/<int:pk>",
        CompanyView.as_view({
            "get": "retrieve", "put": "update", "delete": "delete"
        }),
        name="company-detail",
    ),
]
