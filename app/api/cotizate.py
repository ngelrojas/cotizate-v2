from core.user import User
from core.profileCompany import ProfileCompany


class ActiveUser:
    """all about user"""

    def __init__(self):
        pass

    def currentUser(self, request):
        """get a current user is not deleted"""
        user = User.objects.get(id=request.user.id, deleted=False)
        return user


class ProfileComplete:
    """all about profile user"""

    def __init__(self):
        pass

    def currentProfile(self, profile, request):
        pro = profile.objects.get(user=request.user)
        return pro

    def isComplete(self, profile, request):
        """is profile complete"""
        profile = self.currentProfile(profile, request)
        return profile.complete

    def update_profile(self, profile, request, country, city):
        """
        update complete field to True
        return True means is updated recently
        return False means was updated
        """
        prof = self.currentProfile(profile, request)
        prof.cinit = request.data.get("cinit")
        prof.address = request.data.get("address")
        prof.number_address = request.data.get("number_address")
        prof.neightbordhood = request.data.get("neightbordhood")
        prof.cellphone = request.data.get("cellphone")
        prof.telephone = request.data.get("telephone")
        prof.description = request.data.get("description")
        prof.representative = request.data.get("representative")
        prof.complete = True
        prof.current_position = request.data.get("current_position")
        prof.headline = request.data.get("headline")
        prof.birthdate = request.data.get("birthdate")
        prof.countries = country
        prof.cities = city
        prof.photo = request.data.get("photo")
        prof.save()
        return True


class HelperCompany:
    def getCurrentCompany(self, request, pk):
        current_pro = ProfileCompany.objects.get(id=pk, user=request.user)
        return current_pro
