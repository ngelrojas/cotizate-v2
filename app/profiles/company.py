from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from api.cotizate import ProfileComplete
from api.cotizate import HelperCompany
from core.profile import CompanyProfile
from core.profile import PersonalProfile
from core.queries.helperCompany import HelperQueryCompany
from .companySerializers import CompanySerializer


class UpdateCompanyView(viewsets.ModelViewSet):
    """class update current profile company"""

    serializer_class = CompanySerializer
    queryset = CompanyProfile.objects.all()

    def list(self, request):
        """list all companies about current user"""
        try:
            queryset = HelperQueryCompany.getAllCompanies(self, request)
            serializer = self.serializer_class(queryset, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except CompanyProfile.DoesNotExist as err:
            return Response({"error": f"{err}"}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        """create a company"""
        try:
            profile = ProfileComplete()
            is_pprofile = profile.isComplete(PersonalProfile, self.request)
            if is_pprofile:
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(user=request.user)
                    return Response(
                        {"data": "company profiel created."},
                        status=status.HTTP_201_CREATED,
                    )
        except CompanyProfile.DoesNotExist as err:
            return Response({"error": f"{err}"}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """retrieve current company profile"""
        try:
            current_company = HelperCompany.getCurrentCompany(self, request, pk)
            serializer = self.serializer_class(current_company)
            return Response(serializer.data)
        except CompanyProfile.DoesNotExist as err:
            return Response({"error": f"{err}"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """update current company profile"""
        try:
            current_company = HelperCompany.getCurrentCompany(self, request, pk)
            serializer = self.serializer_class(
                current_company, data=request.data, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"data": "company profile updated."}, status=status.HTTP_200_OK,
                )
        except CompanyProfile.DoesNotExist as err:
            return Response({"error": f"{err}"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """delete current company"""
        try:
            HelperQueryCompany.deleteCompany(self, request, pk)
            return Response({"data": "company deleted."}, status=status.HTTP_200_OK)
        except CompanyProfile.DoesNotExist as err:
            return Response({"error": f"{err}"}, status=status.HTTP_400_BAD_REQUEST)
