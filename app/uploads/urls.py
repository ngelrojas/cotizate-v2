from django.urls import path
from uploads import views

app_name = "upload"

urlpatterns = [
    path("upload", views.UploadView.as_view({"post": "create"}), name="uploads"),
    path(
        "upload/<int:pk>",
        views.UploadView.as_view({"get": "retrieve"}),
        name="uploads-details",
    ),
]
