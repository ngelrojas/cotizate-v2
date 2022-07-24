import json
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import status
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import CategorySerializer
from core.category import Category
from core.campaing import Campaing
from core.queries.categoryQuery import CategoryQuery
from core.queries.campaingQuery import CampaingPrivateQuery
from campaings.body.serializers import CampaingBodySerializer
from campaings.body.serializers import CampaingBodySearch


class CategoryView(viewsets.ModelViewSet):
    """
    list
        - list all categories
    retrieve
        - get a category
    """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "name",
    ]


class CategorySearch(ListAPIView):
    """
    list:
        - relationship between category and campaing
        - searching in a category and title from campaing
    """

    serializer_class = CampaingBodySearch
    queryset = Campaing.objects.all()
    permission_classes = (AllowAny,)

    def list(self, request, the_slug, search_name):
        try:
            list_header = CategoryQuery.get_list_camp_header(the_slug)
            public = 5
            resp_list_camps = []

            for header_camp in list_header:

                camp = Campaing.objects.filter(
                    header=header_camp, title__icontains=search_name, status=public
                )

                if camp:
                    serializer = CampaingBodySearch(camp, many=True)
                    resp_list_camps.append(serializer.data)

            return Response({"data": resp_list_camps}, status=status.HTTP_200_OK)

        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )
