from django.urls import path
from .company import CompanyView


app_name = "profile-company"

urlpatterns = [
    path(
        "profile/company",
        CompanyView.as_view({"post": "create"}),
        name="profile-company",
    ),
    path(
        "profile/company/<int:pk>",
        CompanyView.as_view({"get": "retrieve", "put": "update", "delete": "delete"}),
        name="profile-company-detail",
    ),
]