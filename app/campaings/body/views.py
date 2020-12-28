from datetime import datetime
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.campaing import CampaingBody
from core.queries.campaingBodyQuery import CampaingBodyQuery as CampBQ
from core.queries.campaingQuery import CampaingPrivateQuery as CampPBQ
from core.currency import Currency
from .serializers import CampaingBodySerializer
from ..public.serializers import CampaingPublicSerializer
from ..component.CmpHeader import CampHeaderComp
import pdb

class CampaingsBody(viewsets.ModelViewSet):
    """Campaing
    - list: list campaing to current user
    - create: create campaing to current user
    - retrieve: retrieve campaing to current user and ID campaing
    - update: update campaing to current user and ID campaing
    """

    serializer_class = CampaingBodySerializer
    queryset = CampaingBody.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request, pk):
        try:
            list_header = CampPBQ.get_list_camp_header(request)
            list_camp = []
            list_camp = CampPBQ.list_camps(list_header, pk)
            serializer = self.serializer_class(list_camp, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        """create campaing body current user"""
        try:
            print(request.data)
            pdb.set_trace()
            return Response({"data": "ok"})
            # resp = CampHeaderComp.saving_campaing(request)
            # if resp:
            #     return Response(
            #         {"data": True, "msg": "campaing body saved."},
            #         status=status.HTTP_201_CREATED,
            #     )

            # return Response(
            #         {"data": False, "msg": f"{resp}"},
            #         status=status.HTTP_400_BAD_REQUEST,
            #     )
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
        except CampaingBody.DoesNotExist as err:
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
