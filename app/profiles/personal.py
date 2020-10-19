from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from api.cotizate import ProfileComplete
from core.profile import PersonalProfile as PerPF
from .serializers import PersonalSerializer


class PersonalProfileView(viewsets.ModelViewSet):
    """create profile current user"""

    serializer_class = PersonalSerializer
    queryset = PerPF.objects.all()

    def create(self, request):
        """create personal profile"""
        try:
            send_data = {}
            send_data = request.data
            send_data.update(request.user)
            serializer = self.serializer_class(data=send_data)
            if serializer.is_valid(raise_exception=True):
                pp = serializer.save()
                return Response(
                    {"data": pp.id, "msg": "personal profile created."},
                    status=status.HTTP_201_CREATED,
                )
        except PerPF.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTT_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """retrieve profile current user"""
        try:
            current_profile = PerPF.objects.get(user=request.user)
            serializer = self.serializer_class(current_profile)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk):
        """update profile current user"""
        try:
            current_profile = PerPF.objects.get(user=pk)
            serializer = self.serializer_class(
                current_profile, data=request.data, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                pro_complete = ProfileComplete()
                complete = pro_complete.update_profile(PerPF, request)
                return Response(
                    {"data": complete, "msg": "profile updated."},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"data": False, "msg": "something wrong happend"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except PerPF.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
