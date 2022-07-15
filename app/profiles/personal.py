from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from api.cotizate import ProfileComplete
from core.profile import PersonalProfile as PerPF
from core.country import Country
from core.city import City
from core.queries.profilesQuery import ProfilesQuery
from .serializers import PersonalSerializer


class PersonalProfileView(viewsets.ModelViewSet):
    """create profile current user"""

    serializer_class = PersonalSerializer
    queryset = PerPF.objects.all()

    def list(self, request):
        """list all personal profiles"""
        try:
            current_profiles = PersonalProfile.get_all(request) 
            serializer = self.serializer_class(current_profiles, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk):
        """retrieve profile current user"""
        try:
            current_profile = PersonalProfile.get_by_id(request, pk) 
            serializer = self.serializer_class(current_profile)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        """create personal profile"""
        try:

            prof_personal = PersonalProfile.created(request) 
            return Response(
                {"data": prof_personal, "msg": "personal profile created."},
                status=status.HTTP_201_CREATED,
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )


    def update(self, request, pk):
        """update profile current user"""
        try:
            complete = PersonalProfile.updated(request, pk) 

            return Response(
                {"data": complete, "msg": "personal profile updated."},
                status=status.HTTP_200_OK,
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        """delete current personal profile"""
        try:
            erase = PersonalProfile.erase(request, pk)
            return Response(
                {"data": erase, "msg": "personal profile Deleted"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"},
                status=status.HTTP_404_NOT_FOUND
            )
