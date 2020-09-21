from rest_framework import viewsets
from rest_framework import filters
from .serializers import CountrySerializer
from core.country import Country


class CountryView(viewsets.ModelViewSet):
    """
    list
        - list all countries
    retrieve
        - get a country
    """

    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "name",
    ]
