from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from api.cotizate import ProfileComplete
from core.profileAssociation import ProfileAssociation
from .serializers import AssociationSerializer


class AssociationView(viewsets.ModelViewSet):
    """create profile current user"""

    serializer_class = AssociationSerializer
    queryset = ProfileAssociation.objects.all()

    def create(self, request):
        """create personal association"""
        try:
            send_data = {}
            send_data = request.data
            send_data.update(request.user)
            serializer = self.serializer_class(data=send_data)
            if serializer.is_valid(raise_exception=True):
                pa = serializer.save()
                return Response(
                    {"data": pa.id, "msg": "profile association created."},
                    status=status.HTTP_201_CREATED,
                )
        except ProfileAssociation.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTT_400_BAD_REQUEST
            )

    def retrieve(self, pk):
        """retrieve profile current user"""
        try:
            current_profile = ProfileAssociation.objects.get(user=pk)
            serializer = self.serializer_class(current_profile)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except ProfileAssociation.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk):
        """update profile current user"""
        try:
            current_profile = ProfileAssociation.objects.get(user=pk)
            serializer = self.serializer_class(
                current_profile, data=request.data, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                pro_complete = ProfileComplete()
                complete = pro_complete.update_profile(ProfileAssociation, request)
                return Response(
                    {"data": complete, "msg": "profile updated."},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"data": False, "msg": "something wrong happend"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except ProfileAssociation.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
