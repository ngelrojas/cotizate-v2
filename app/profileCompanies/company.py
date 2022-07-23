from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
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
            list_company = ProfileCompany.objects.filter(
                user=request.user,
                delete=False
            )
            serializer = self.serializer_class(list_company, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        """create personal company"""
        try:
            # prof_create_company = ProfilesQuery()
            countries = Country.objects.get(id=request.data.get("country_id"))
            cities = City.objects.get(id=request.data.get("city_id"))
            prof_company = ProfileCompany.created(request, countries, cities)

            return Response(
                {"data": prof_company, "msg": "profile company created."},
                status=status.HTTP_201_CREATED,
            )
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """
        retrieve profile company current user
        pk is the ID current profile user
        pc is the ID the profile company the current user
        """
        try:
            current_profile = ProfileCompany.objects.get(id=pk, user=request.user)
            serializer = self.serializer_class(current_profile)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk=None):
        """update profile company current user"""
        try:
            # prof_comp = ProfilesQuery()
            countries = Country.objects.get(id=request.data.get("country_id"))
            cities = City.objects.get(id=request.data.get("city_id"))
            complete = ProfileCompany.updated(request, countries, cities, pk)

            return Response(
                {"data": complete, "msg": "profile updated."},
                status=status.HTTP_200_OK,
            )

        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk=None):
        try:
            prof_comp = ProfileCompany.erase(request, pk) 

            return Response(
                {"data": prof_comp, "msg": "profile company deleted"},
                status=status.HTTP_204_NO_CONTENT
            )

        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"},
                status=status.HTTP_400_BAD_REQUEST
            )
