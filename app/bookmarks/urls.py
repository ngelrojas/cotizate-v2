from django.urls import path
from .views import BookMarkView

app_name = "book-mark"

urlpatterns = [
    path(
        "bookmark",
        BookMarkView.as_view({"get": "list", "post": "create"}),
        name="bookmark",
    ),
    path(
        "bookmark/<int:pk>",
        BookMarkView.as_view({"get": "retrieve", "put": "update"}),
        name="bookmark-detail",
    ),
]
