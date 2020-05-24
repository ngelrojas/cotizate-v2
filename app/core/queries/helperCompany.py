from core.profile import CompanyProfile


class HelperQueryCompany:
    def getAllCompanies(self, request):
        result = CompanyProfile.objects.filter(user=request.user)
        return result

    def deleteCompany(self, request, pk):
        result = CompanyProfile.objects.get(id=pk, user=request.user)
        result.delete()
        return True
