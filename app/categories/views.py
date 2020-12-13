from rest_framework import viewsets
from rest_framework import status
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import CategorySerializer
from core.category import Category
from core.queries.categoryQuery import CategoryQuery
from core.queries.campaingQuery import CampaingPrivateQuery
from campaings.body.serializers import CampaingBodySerializer


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

    def retrieve(self, request, the_slug):
        try:
            list_header = CategoryQuery.get_list_camp_header(the_slug)
            list_camp = []
            list_camp = CampaingPrivateQuery.list_camps(list_header, 5)
            serializer = CampaingBodySerializer(list_camp, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )
