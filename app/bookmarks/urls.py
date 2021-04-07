from django.urls import path
from .views import BookMarkView

app_name = "book-mark"

urlpatterns = [
    path(
        "book-mark",
        BookMarkView.as_view({"get": "list", "post": "create"}),
        name="book-mark",
    ),
    path(
        "book-mark/<int:pk>",
        BookMarkView.as_view({"get": "retrieve", "put": "update"}),
        name="detail-book-mark",
    ),
]
