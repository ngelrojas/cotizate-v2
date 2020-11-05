from core.profileCompany import ProfileCompany
from core.profile import PersonalProfile


class ProfilesQuery:
    """profiles query"""

    @classmethod
    def saving_profile_company(cls, request, country, city):
        """save company profile"""
        pcompany = ProfileCompany.objects.create(
            cinit=request.data.get("cinit"),
            address=request.data.get("address"),
            number_address=request.data.get("number_address"),
            neightbordhood=request.data.get("neightbordhood"),
            cellphone=request.data.get("cellphone"),
            telephone=request.data.get("telephone"),
            description=request.data.get("description"),
            representative=request.data.get("representative"),
            complete=request.data.get("complete"),
            company_name=request.data.get("company_name"),
            countries=country,
            cities=city,
            user=request.user,
        )
        return pcompany

    @classmethod
    def saving_profile_personal(cls, request, country, city):
        """save profile personal"""
        ppersonal = PersonalProfile.objects.create(
            cinit=request.data.get("cinit"),
            address=request.data.get("address"),
            number_address=request.data.get("number_address"),
            neightbordhood=request.data.get("neightbordhood"),
            cellphone=request.data.get("cellphone"),
            telephone=request.data.get("telephone"),
            description=request.data.get("description"),
            representative=request.data.get("representative"),
            complete=request.data.get("complete"),
            company_name=request.data.get("company_name"),
            photo=request.data.get("photo"),
            current_position=request.data.get("current_position"),
            headline=request.data.get("headline"),
            countries=country,
            cities=city,
            user=request.user,
        )
        return ppersonal
