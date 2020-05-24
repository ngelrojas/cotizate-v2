from rest_framework import viewsets
from rest_framework import filters
from .serializers import TagSerializer
from core.tag import Tag


class TagView(viewsets.ModelViewSet):
    """
    list
        - list all tags
    retrieve
        - get a tags
    """
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
