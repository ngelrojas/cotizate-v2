from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from api.cotizate import ProfileComplete
from core.profileCompany import ProfileCompany
from core.queries.profilesQuery import ProfilesQuery
from core.country import Country
from core.city import City
from .serializers import CompanySerializer


class CompanyView(viewsets.ModelViewSet):
    """create profile current user"""

    serializer_class = CompanySerializer
    queryset = ProfileCompany.objects.all()

    def list(self, request):
        """all companies about the current user"""
        try:
            list_company = ProfileCompany.objects.filter(user=request.user)
            serializer = self.serializer_class(list_company, many=True)
            return Response({"data": serializer}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        """create personal company"""
        try:
            countries = Country.objects.get(id=int(request.data.get("countries")))
            cities = City.objects.get(id=int(request.data.get("cities")))
            prof_company = ProfilesQuery.saving_profile_company(
                request, countries, cities
            )
            # prof_company = request.data
            return Response(
                {"data": prof_company, "msg": "profile company created."},
                status=status.HTTP_201_CREATED,
            )
        except ProfileCompany.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTT_400_BAD_REQUEST
            )

    def retrieve(self, pk):
        """retrieve profile company current user"""
        try:
            current_profile = ProfileCompany.objects.get(user=pk)
            serializer = self.serializer_class(current_profile)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except ProfileCompany.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk):
        """update profile company current user"""
        try:
            current_profile = ProfileCompany.objects.get(user=pk)
            serializer = self.serializer_class(
                current_profile, data=request.data, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                pro_complete = ProfileComplete()
                complete = pro_complete.update_profile(ProfileCompany, request)
                return Response(
                    {"data": complete, "msg": "profile updated."},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"data": False, "msg": "something wrong happend"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except ProfileCompany.DoesNotExist as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )
