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


class CategoryView(viewsets.ModelViewSet): 

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # permission_classes = (AllowAny,)
    # filter_backends = [filters.SearchFilter]
    # search_fields = [
    #     "name",
    # ]

    def list(self, request):
        try:
            resp = Category.get_all()
            serializer = self.serializer_class(resp, many=True)
            return Response(
                    {"data": serializer.data},
                    status = status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                    {"data": None, "msg": f"{e}"},
                    status = status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        try:
            resp = Category.get_category(pk)
            serializer = self.serializer_class(resp)
            return Response(
                    {"data": serializer.data},
                    status = status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                    {"data": None, "msg": f"{e}"},
                    status = status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        try:
            resp = Category.created(request)
            return Response(
                    {"data": resp, "msg": "category created"},
                    status = status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                    {"data": None, "msg": f"{e}"},
                    status = status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk):
        try:
            resp = Category.updated(request, pk)
            return Response(
                    {"data": resp, "msg": "category updated"},
                    status = status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                    {"data": None, "msg": f"{e}"},
                    status = status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        try:
            resp = Category.erase(request, pk)
            return Response(
                    {"data": resp, "msg": "category deleted"},
                    status = status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            return Response(
                    {"data": None, "msg": f"{e}"},
                    status = status.HTTP_400_BAD_REQUEST
                    )


