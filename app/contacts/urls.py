from django.urls import path
from contacts import views

app_name = "contacts"

urlpatterns = [
    path(
        "contacts",
        views.ContactView.as_view({"get": "list", "post": "create"}),
        name="contacts",
    ),
    path(
        "contacts/<int:pk>",
        views.ContactView.as_view({"get": "retrieve"}),
        name="contacts-list",
    ),
]
