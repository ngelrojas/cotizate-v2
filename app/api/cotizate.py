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
        pro = profile.objects.get(id=request.user.id)
        return pro

    def isComplete(self, profile, request):
        """is profile complete"""
        profile = self.currentProfile(profile, request)
        return profile.complete

    def update_profile(self, profile, request):
        """
        update complete field to True
        return True means is updated recently
        return False means was updated
        """
        is_complete = self.isComplete(profile, request)
        if not is_complete:
            prof = self.currentProfile(profile, request)
            prof.complete = True
            prof.save()
            return True
        return False


class HelperCompany:
    def getCurrentCompany(self, request, pk):
        current_pro = ProfileCompany.objects.get(id=pk, user=request.user)
        return current_pro
