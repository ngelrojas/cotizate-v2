from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.campaing import CampaingHeader
from core.queries.campaingQuery import CampaingHeaderQuery as CampHQ
from core.profile import PersonalProfile
from .serializers import CampaingHeaderSerializer


class CampaingsHeader(viewsets.ModelViewSet):
    """Campaing
    - list: list campaing to current user
    - create: create campaing to current user
    - retrieve: retrieve campaing to current user and ID campaing
    - update: update campaing to current user and ID campaing
    """

    serializer_class = CampaingHeaderSerializer
    queryset = CampaingHeader.objects.all()

    def list(self, request):
        """list all campaings to current user"""
        try:
            list_campaing = CampHQ.get_list_ch(request)
            serializer = self.serializer_class(list_campaing, many=True)
            return Response(
                {"data": serializer.data, "msg": "ok"}, status=status.HTTP_200_OK
            )
        except CampaingHeader.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        """create campaing to current user"""
        try:
            send_data = {
                "user": request.user,
                "category": request.data.get("category"),
                "city": request.data.get("city"),
                "qty_day": request.data.get("qty_day"),
                "amount": request.data.get("amount"),
                "role": request.data.get("role"),
            }

            serializer = self.serializer_class(data=send_data)
            if serializer.is_valid(raise_exception=True):
                camp_header = serializer.save()
                return Response(
                    {"data": camp_header.id, "msg": "campaing header is saved."},
                    status=status.HTTP_201_CREATED,
                )

        except CampaingHeader.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk):
        """retrieve campaing to current user and ID campaing"""
        try:
            current_campaingh = CampHQ.retrieve_ch(request, pk)
            serializer = self.serializer_class(current_campaingh)
            return Response(
                {"data": serializer.data, "msg": "ok"}, status=status.HTTP_200_OK
            )
        except CampaingHeader.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk):
        """update current campaing to current user and ID campaing"""
        try:
            current_campaingh = CampHQ.retrieve_ch(request, pk)
            serializer = self.serializer_class(
                current_campaingh, data=request.data, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                camp_header = serializer.save()
                return Response(
                    {"data": camp_header.id, "msg": "campaing header updated."},
                    status=status.HTTP_200_OK,
                )
        except CampaingHeader.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        """retrieve campaing to current user and ID campaing"""
        try:
            current_campaingh = CampHQ.retrieve_ch(request, pk)
            current_campaingh.delete()
            return Response(
                {"data": True, "msg": "campaing header deleted."},
                status=status.HTTP_204_NOT_CONTENT,
            )
        except CampaingHeader.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
