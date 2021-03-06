from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from api.cotizate import ProfileComplete
from core.profileCompany import ProfileCompany
from core.queries.profilesQuery import ProfilesQuery
from core.country import Country
from core.city import City
from core.profile import PersonalProfile
from .serializers import CompanySerializer


class CompanyView(viewsets.ModelViewSet):
    """create profile current user"""

    serializer_class = CompanySerializer
    queryset = ProfileCompany.objects.all()

    def list(self, request):
        """all companies about the current user"""
        try:
            profile_per = PersonalProfile.objects.get(user=request.user)
            list_company = ProfileCompany.objects.filter(profiles=profile_per)
            serializer = self.serializer_class(list_company, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        """create personal company"""
        try:
            prof_create_company = ProfilesQuery()
            countries = Country.objects.get(id=int(request.data.get("countries")))
            cities = City.objects.get(id=int(request.data.get("cities")))
            prof_company = prof_create_company.saving_profile_company(
                request, countries, cities
            )
            return Response(
                {"data": prof_company, "msg": "profile company created."},
                status=status.HTTP_201_CREATED,
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTT_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None, pc=None):
        """
        retrieve profile company current user
        pk is the ID current profile user
        pc is the ID the profile company the current user
        """
        try:
            profile_per = PersonalProfile.objects.get(id=pk)
            current_profile = ProfileCompany.objects.get(id=pc, profiles=profile_per)
            serializer = self.serializer_class(current_profile)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except ProfileCompany.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk=None, pc=None):
        """update profile company current user"""
        try:
            prof_comp = ProfilesQuery()
            countries = Country.objects.get(id=int(request.data.get("countries")))
            cities = City.objects.get(id=int(request.data.get("cities")))
            complete = prof_comp.update_profile_company(pk, pc, request, countries, cities)

            return Response(
                {"data": complete, "msg": "profile updated."},
                status=status.HTTP_200_OK,
            )

        except ProfileCompany.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
