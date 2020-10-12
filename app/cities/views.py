from rest_framework import viewsets
from rest_framework import filters, status
from rest_framework.response import Response
from .serializers import CitySerializer
from core.city import City
from core.queries.citiesQuery import CitiesQuery


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

    def retrieve(self, request, pk):
        """retrieve city by ID and ID country"""
        try:
            current_city = CitiesQuery.retrieve_cities(
                request.data.get("country_id"), pk
            )
            serializer = self.serializer_class(current_city)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except City.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
