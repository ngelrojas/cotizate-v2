from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .queries.campaing_query import CampaingQuery
from .serializers import CampaingSerializer
from core.category import Category


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
            category = Category.get_category(request.data.get("category_id"))
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


class CampaingView3(viewsets.ModelViewSet):
    serializer_class = CampaingSerializer
    queryset = CampaingQuery.get_all()

    def list(self, flag=None):
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

    def retrieve(self, role=None):
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

    def list(self, dinit, dfinal):
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

    def retrieve(self, dinit, dfinal):
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

    def retrieve(self, status=None, flag=None):
        try:
            resp = CampaingQuery.get_by_status_flag(status, flag)
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
