from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.campaing import CampaingHeader
from core.queries.campaingQuery import CampaingHeaderQuery as CampHQ
from core.profile import PersonalProfile
from .serializers import CampaingHeaderSerializer
from .serializers import CHDetailSerializer


class CampaingsHeader(viewsets.ModelViewSet):
    """Campaing
    - list: list campaing to current user
    - create: create campaing to current user
    - retrieve: retrieve campaing to current user and ID campaing
    - update: update campaing to current user and ID campaing
    """

    serializer_class = CampaingHeaderSerializer
    queryset = CampaingHeader.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        """list all campaings to current user"""
        try:
            list_campaing = CampHQ.get_list_ch(request)
            serializer = self.serializer_class(list_campaing, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except CampaingHeader.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        """create campaing to current user"""
        try:
            send_data = {
                "user": request.user.id,
                "category": request.data.get("category"),
                "city": request.data.get("city"),
                "qty_day": request.data.get("qty_day"),
                "amount": request.data.get("amount"),
                "role": request.data.get("role"),
            }
            serializer = self.get_serializer(data=send_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {"data": serializer.data},
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        except CampaingHeader.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def perform_create(self, serializer):
        """create with current user"""
        serializer.save(user=self.request.user)

    def retrieve(self, request, pk):
        """retrieve campaing to current user and ID campaing"""
        try:
            current_campaingh = CampHQ.retrieve_ch(request, pk)
            serializer = CHDetailSerializer(current_campaingh)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
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
                serializer.save()
                return Response(
                    {"data": serializer.data},
                    status=status.HTTP_200_OK,
                )
        except CampaingHeader.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, pk):
        """retrieve campaing to current user and ID campaing"""
        try:
            current_campaingh = CampHQ.retrieve_ch(request, pk)
            current_campaingh.delete()
            return Response(
                {"data": "campaing deleted."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except CampaingHeader.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
