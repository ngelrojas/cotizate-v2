from django.urls import path
from countries import views

app_name = "country"

urlpatterns = [
    path("country", views.CountryView.as_view({"get": "list"}), name="countries")
]
