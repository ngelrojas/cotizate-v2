from bookmarks import serializers
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .queries.campaing_query import CampaingQuery
from .serializers import CampaingSerializer
from core.category import Category
from core.city import City


class CampaingView1(viewsets.ModelViewSet):
    serializer_class = CampaingSerializer
    queryset = CampaingQuery.get_all()

    def list(self, request):
        try:
            resp = CampaingQuery.get_all()
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
            category = Category.get_category(pk)
            resp = CampaingQuery.get_by_category(category)
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

class CampaingView2(viewsets.ModelViewSet):
    serializer_class = CampaingSerializer
    queryset = CampaingQuery.get_all()

    def list(self, request, pk=None):
        try:
            city = City.get_by_id(pk)
            resp = CampaingQuery.get_by_city(city)
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

    def retrieve(self, request, title=None):
        try:
            resp = CampaingQuery.get_by_title(title)
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


class CampaingView3(viewsets.ModelViewSet):
    serializer_class = CampaingSerializer
    queryset = CampaingQuery.get_all()

    def list(self, request, flag=None):
        try:
            resp = CampaingQuery.get_by_flag(flag)
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

    def retrieve(self, request, role=None):
        try:
            resp = CampaingQuery.get_by_role(role)
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


class CampaingView4(viewsets.ModelViewSet):
    serializer_class = CampaingSerializer
    queryset = CampaingQuery.get_all()

    def list(self, request, dinit, dfinal):
        try:
            resp = CampaingQuery.get_by_created(dinit, dfinal)
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

    def retrieve(self, request, dinit, dfinal):
        try:
            resp = CampaingQuery.get_by_ended(dinit, dfinal)
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


class CampaingView5(viewsets.ModelViewSet):
    serializer_class = CampaingSerializer
    queryset = CampaingQuery.get_all()

    def list(self, request, field_status=None, flag=None):
        try:
            resp = CampaingQuery.get_by_status_flag(field_status, flag)
            serializer = self.serializer_class(resp, many=True)
            return Response(
                    {"data": serializer.data},
                    status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                    {"data": None, "msg": f"{e}"},
                    status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, title=None):
        try:
            resp = CampaingQuery.get_by_exact_title(title)
            serializer = self.serializer_class(resp)
            return Response(
                    {"data": serializer.data},
                    status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                    {"data": None, "msg": f"{e}"},
                    status=status.HTTP_400_BAD_REQUEST
            )


class CampaingView6(viewsets.ModelViewSet):
    serializer_class = CampaingSerializer
    queryset = CampaingQuery.get_all()

    def retrieve(self, request, campaing_id):
        try:
            resp = CampaingQuery.get_by_campaing_id(campaing_id)
            serializer = self.serializer_class(resp)
            return Response(
                    {"data": serializer.data},
                    status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                    {"data": None, "msg": f"{e}"},
                    status=status.HTTP_400_BAD_REQUEST   
            )
