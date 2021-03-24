import string
import random
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.campaing import CampaingHeader
from core.queries.campaingQuery import CampaingHeaderQuery as CampHQ
from core.profile import PersonalProfile
from core.category import Category
from core.city import City
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

            category = Category.objects.get(id=request.data.get("category"))
            city = City.objects.get(id=request.data.get("city"))
            qty_day = request.data.get("qty_day")
            role = request.data.get("role")
            str_cat = str(category.id)
            str_ci = str(city.id)
            str_q = str(qty_day)
            str_r = str(role)
            amount = float(request.data.get("amount"))
            code = f"CAMP{str_cat}{str_ci}{str_q}{str_r}{str(request.user.id)}"

            send_data = {
                "user": request.user,
                "category": category,
                "city": city,
                "qty_day": qty_day,
                "qty_day_left": request.data.get("qty_day"),
                "amount": amount,
                "role": role,
                "code_campaing": code,
            }

            resp_header = CampHQ.create_header(self, send_data)

            if resp_header is True:
                return Response(
                    {"data": "header is created"}, status=status.HTTP_201_CREATED
                )

            return Response(
                {"data": False, "msg": f"{resp_header}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as err:
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
