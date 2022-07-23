import string
import random
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.campaing import Campaing
from core.profile import PersonalProfile
from core.category import Category
from core.city import City
from core.currency import Currency
from .serializers import CampaingSerializer


class CampaingView(viewsets.ModelViewSet):

    serializer_class = CampaingSerializer
    queryset = Campaing.objects.all()

    def list(self, request):
        try:
            list_camp = Campaing.get_all_campaings(request)
            serializer = self.serializer_class(list_camp, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                    {"data": False, "msg": f"{e}"},
                    status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        try:
            get_camp = Campaing.get_campaing_id(request, pk)
            serialzer = self.serializer_class(get_camp)
            return Response(
                    {"data": serializer.data},
                    status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                    {"data": False, "msg": f"{e}"},
                    status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        try:
            objcate = Category.objects.get(id=request.data.get("category_id"))
            objcity = City.objects.get(id=request.data.get("city_id"))
            objcurrency = Currency.objects.get(id=request.data.get("currency_id")) 
            objcampaing = Campaing.create(objcate, objcity, objcurrency, request)
            return Response(
                    {"data": objcampaing, "msg": "campaing created"},
                    status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                    {"data": False, "msg": f"{e}"},
                    status=e
            )

    def update(self, request, pk=None):
        try:
            objcate = Category.objects.get(id=request.data.get("category_id"))
            objcity = City.objects.get(id=request.data.get("city_id"))
            objcurrency = Currency.objects.get(id=request.data.get("currency_id"))
            objcampaing = Campaing.updated(objcate, objcity, objcurrency, request, pk)
            return Response(
                    {"data": objcampaing, "msg": "campaing updated"},
                    status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                    {"data": False, "msg": f"{e}"},
                    status=e
            )

    def delete(self, request, pk=None):
        try:
            resp = Campaing.erase(request, pk)
            return Response(
                    {"data": resp, "msg": "campaing is deleted"},
                    status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            return Response(
                    {"data": False, "msg": f"{e}"},
                    status=HTTP_400_BAD_REQUEST
            )
