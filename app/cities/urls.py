from django.urls import path
from cities import views

app_name = "city"

urlpatterns = [
    path("city", views.CityView.as_view(
             {"get": "list"}), 
         name="cities"
    )
]
