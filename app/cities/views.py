from rest_framework import viewsets
from rest_framework import filters
from .serializers import CitySerializer
from core.city import City


class CityView(viewsets.ModelViewSet):
    """
    list
        - list all city
    retrieve
        - get a city
    """

    serializer_class = CitySerializer
    queryset = City.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "name",
    ]
