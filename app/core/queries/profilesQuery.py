from core.profileCompany import ProfileCompany
from core.profile import PersonalProfile


class ProfilesQuery:
    """profiles query"""

    @classmethod
    def saving_profile_company(cls, request, country, city):
        """save company profile"""
        try:
            ProfileCompany.objects.create(
                cinit=request.data.get("cinit"),
                address=request.data.get("address"),
                number_address=request.data.get("number_address"),
                neightbordhood=request.data.get("neightbordhood"),
                cellphone=request.data.get("cellphone"),
                telephone=request.data.get("telephone"),
                description=request.data.get("description"),
                representative=request.data.get("representative"),
                complete=True,
                company_name=request.data.get("company_name"),
                photo=request.data.get("photo"),
                rs_facebook=request.data.get("rs_facebook"),
                rs_twitter=request.data.get("rs_twitter"),
                rs_linkedin=request.data.get("rs_linkedin"),
                rs_another=request.data.get("rs_another"),
                user=request.user,
                countries=country,
                cities=city,
            )
            return True
        except ProfileCompany.DoesNotExist as err:
            return err

    @classmethod
    def update_profile_company(cls, pk, request, country, city):
        """update current company profile"""
        prof_comp = ProfileCompany.objects.get(id=pk, user=request.user)
        prof_comp.cinit = request.data.get("cinit")
        prof_comp.address = request.data.get("address")
        prof_comp.number_address = request.data.get("number_address")
        prof_comp.neightbordhood = request.data.get("neightbordhood")
        prof_comp.cellphone = request.data.get("cellphone")
        prof_comp.telephone = request.data.get("telephone")
        prof_comp.description = request.data.get("description")
        prof_comp.representative = request.data.get("representative")
        prof_comp.complete = True
        prof_comp.company_name = request.data.get("company_name")
        prof_comp.countries = country
        prof_comp.cities = city
        prof_comp.save()
        return True

    @classmethod
    def saving_profile_personal(cls, request, country, city):
        """save profile personal"""
        try:
            PersonalProfile.objects.create(
                cinit=request.data.get("cinit"),
                address=request.data.get("address"),
                number_address=request.data.get("number_address"),
                neightbordhood=request.data.get("neightbordhood"),
                cellphone=request.data.get("cellphone"),
                telephone=request.data.get("telephone"),
                description=request.data.get("description"),
                representative=request.data.get("representative"),
                complete=request.data.get("complete"),
                birthdate=request.data.get("birthdate"),
                photo=request.data.get("photo"),
                current_position=request.data.get("current_position"),
                headline=request.data.get("headline"),
                rs_facebook=request.data.get("rs_facebook"),
                rs_twitter=request.data.get("rs_twitter"),
                rs_linkedin=request.data.get("rs_linkedin"),
                rs_another=request.data.get("rs_another"),
                user=request.user,
                countries=country,
                cities=city,
            )
            return True
        except Exception:
            return False
