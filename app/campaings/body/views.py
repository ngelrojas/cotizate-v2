from datetime import datetime
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.campaing import CampaingBody
from core.queries.campaingBodyQuery import CampaingBodyQuery as CampBQ
from core.currency import Currency
from .serializers import CampaingBodySerializer
from ..component.CmpHeader import CampHeaderComp


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

    def create(self, request):
        """create campaing body current user"""
        try:
            data = CampHeaderComp.saving_campaing(request)
            return Response(
                {"data": data},
                status=status.HTTP_201_CREATED,
            )

        except Exception as err:
            return Response(
                {"data": False, "mgs": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk):
        """retrieve campaing body using header_id and pk=campaing_body"""
        try:
            current_campaing = CampBQ.retrieve_cb(pk, request.data.get("header_id"))
            serializer = self.serializer_class(current_campaing)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

        except CampaingBody.DoesNotExist as err:
            return Response(
                {"data": False, "mgs": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk):
        """update campaing body using header_id and pk=campaing_body"""
        try:
            current_campaing = CampBQ.retrieve_cb(pk, request.data.get("header"))
            serializer = self.serializer_class(
                current_campaing, data=request.data, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": True, "msg": "campaing body updated."},
                    status=status.HTTP_200_OK,
                )
        except CampaingBody.DoesNotExist as err:
            return Response(
                {"data": False, "mgs": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, pk):
        """retrieve campaing to current user and ID campaing"""
        try:
            CampBQ.delete_cb(pk, request.data.get("header_id"))
            return Response(
                {"data": "campaing deleted."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except CampaingBody.DoesNotExist as err:
            return Response(
                {"data": False, "mgs": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
