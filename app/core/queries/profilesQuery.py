from django.core.files.storage import FileSystemStorage
from core.profileCompany import ProfileCompany
from core.profile import PersonalProfile


class ProfilesQuery:
    """profiles query"""

    @classmethod
    def saving_profile_company(cls, request, country, city):
        """save company profile"""
        try:
            profile_per = PersonalProfile.objects.filter(user=request.user).last()
            ProfileCompany.objects.create(
                cinit=request.data.get("cinit"),
                address=request.data.get("address"),
                number_address=request.data.get("number_address"),
                neightbordhood=request.data.get("neightbordhood"),
                cellphone=request.data.get("cellphone"),
                telephone=request.data.get("telephone"),
                description=request.data.get("description"),
                representative=True,
                association_name=request.data.get("association_name"),
                heading=request.data.get("heading"),
                complete=True,
                company_name=request.data.get("company_name"),
                email_company=request.data.get("email_company"),
                photo=request.data.get("photo"),
                rs_facebook=request.data.get("rs_facebook"),
                rs_twitter=request.data.get("rs_twitter"),
                rs_linkedin=request.data.get("rs_linkedin"),
                rs_another=request.data.get("rs_another"),
                institution_type=request.data.get("type_institution"),
                profiles=profile_per,
                countries=country,
                cities=city,
                header=request.data.get("header"),
            )
            return True
        except Exception as err:
            return err

    @classmethod
    def update_profile_company(cls, pk, pc, request, country, city):
        """update current company profile"""
        try:
            # profile_per = PersonalProfile.objects.get(id=pk)
            prof_comp = ProfileCompany.objects.get(id=pc, profiles=pk)
            prof_comp.cinit = request.data.get("cinit")
            prof_comp.heading = request.data.get("heading")
            prof_comp.address = request.data.get("address")
            prof_comp.number_address = request.data.get("number_address")
            prof_comp.neightbordhood = request.data.get("neightbordhood")
            prof_comp.cellphone = request.data.get("cellphone")
            prof_comp.telephone = request.data.get("telephone")
            prof_comp.description = request.data.get("description")
            prof_comp.company_name = request.data.get("company_name")
            prof_comp.email_company = request.data.get("email_company")
            prof_comp.countries = country
            prof_comp.cities = city
            prof_comp.rs_facebook = request.data.get("rs_facebook")
            prof_comp.rs_twitter = request.data.get("rs_twitter")
            prof_comp.rs_linkedin = request.data.get("rs_linkedin")
            prof_comp.rs_another = request.data.get("rs_another")
            prof_comp.institution_type = request.data.get("institution_type")
            prof_comp.save()
            return True
        except ProfileCompany.DoesNotExist as err:
            return err

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
                header=request.data.get("header"),
            )
            return True
        except Exception as e:
            return e

    @classmethod
    def update_profile_personal(cls, pk, request, country, city):
        """save profile personal"""
        try:
            profile_per = PersonalProfile.objects.get(id=pk, user=request.user)
            profile_per.cinit = request.data.get("cinit")
            profile_per.address = request.data.get("address")
            profile_per.number_address = request.data.get("number_address")
            profile_per.neightbordhood = request.data.get("neightbordhood")
            profile_per.cellphone = request.data.get("cellphone")
            profile_per.telephone = request.data.get("telephone")
            profile_per.description = request.data.get("description")
            profile_per.birthdate = request.data.get("birthdate")
            profile_per.photo = request.data.get("photo")
            profile_per.current_position = request.data.get("current_position")
            profile_per.headline = request.data.get("headline")
            profile_per.rs_facebook = request.data.get("rs_facebook")
            profile_per.rs_twitter = request.data.get("rs_twitter")
            profile_per.rs_linkedin = request.data.get("rs_linkedin")
            profile_per.rs_another = request.data.get("rs_another")
            profile_per.countries = country
            profile_per.cities = city
            profile_per.save()
            return True
        except Exception:
            return False


class ProfileQueryCompany:
    """profile company query"""

    @staticmethod
    def get_profile_company(current_profiles):
        """get profile company"""
        try:
            return ProfileCompany.objects.filter(profiles=current_profiles).last()
        except Exception:
            return 0
