from datetime import datetime
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.campaing import Campaing
from core.queries.campaingBodyQuery import CampaingBodyQuery as CampBQ
from core.queries.campaingQuery import CampaingPrivateQuery as CampPBQ
from core.currency import Currency
from .serializers import CampaingBodySerializer
from ..public.serializers import CampaingPublicSerializer
from ..component.CmpHeader import CampHeaderComp


class CampaingsBody(viewsets.ModelViewSet):
    """Campaing
    - list: list campaing to current userq
    - create: create campaing to current user
    - retrieve: retrieve campaing to current user and ID campaing
    - update: update campaing to current user and ID campaing
    """

    serializer_class = CampaingBodySerializer
    queryset = Campaing.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request, pk):
        """pk=status campaing"""
        try:
            resp_camp = []
            list_header = CampPBQ.get_list_camp_header(request)

            for header_camp in list_header:

                camp = Campaing.objects.filter(header_id=header_camp, status=pk)

                if camp:
                    serializer = self.serializer_class(camp, many=True)
                    resp_camp.extend(serializer.data)

            return Response({"data": resp_camp}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        """create campaing body current user"""
        try:
            resp = CampHeaderComp.saving_campaing(request)
            if resp:
                return Response(
                    {"data": True, "msg": "campaing body saved."},
                    status=status.HTTP_201_CREATED,
                )

        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """retrieve campaing body using header=header_id and pk=campaing_body_id"""
        try:
            current_campaing = CampBQ.retrieve_cb(pk, request.data.get("header_id"))
            serializer = self.serializer_class(current_campaing)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

        except Exception as err:
            return Response(
                {"data": False, "mgs": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk=None):
        """update campaing body using header_id and pk=campaing_body"""
        try:
            CampHeaderComp.updating_campaing(request, pk)
            return Response(
                {"data": True, "msg": "campaing body updated."},
                status=status.HTTP_200_OK,
            )
        except Exception as err:
            return Response(
                {"data": False, "mgs": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, pk=None):
        """delete campaing body using current header campaing"""
        try:
            current_campaing = CampBQ.delete_cb(pk, request.data.get("header_id"))
            return Response(
                {"data": current_campaing, "msg": "campaing deleted."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception as err:
            return Response(
                {"data": False, "mgs": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )


class CampaingStatus(viewsets.ModelViewSet):
    """
    update status campaings
    """

    serializer_class = CampaingBodySerializer
    queryset = Campaing.objects.all()
    permission_classes = (IsAuthenticated,)

    def update(self, request, pk=None):
        """
        update status from current user
        @params request: user
        @params pk: campaing.id
        """
        try:
            # CampHeaderComp.updating_campaing(request, pk)
            campaing_obj = Campaing.objects.get(id=pk)
            campaing_obj.status = 3
            campaing_obj.save()

            return Response(
                {"data": True, "msg": "campaing status updated."},
                status=status.HTTP_200_OK,
            )

        except Exception as err:
            return Response(
                {"data": False, "mgs": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
