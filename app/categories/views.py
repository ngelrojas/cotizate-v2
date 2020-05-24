from rest_framework import viewsets
from rest_framework import filters
from .serializers import CategorySerializer
from core.category import Category


class CategoryView(viewsets.ModelViewSet):
    """
    list
        - list all categories
    retrieve
        - get a category
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
