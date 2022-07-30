from django.urls import path
from .views import CategoryView 

app_name = "category"

urlpatterns = [
    path("category", 
        CategoryView.as_view({"get": "list", "post": "create"}), 
        name="categories"),
    path(
        "category/<slug:the_slug>",
        CategoryView.as_view(
            {"get": "retrieve", "put": "update", "delete": "delete"}),
        name="category-detail",
    ),
    # path(
    #     "category/<slug:the_slug>/<str:search_name>",
    #     views.CategorySearch.as_view(),
    #     name="category-detail-search",
    # ),
]
