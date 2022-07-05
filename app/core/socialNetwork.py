from django.db import models
from .abstract import AbstractSocialNetwork
from .profile import PersonalProfile
from .profileCompany import ProfileCompany


class SocialNetworkPP(AbstractSocialNetwork):
    """social network personal profile"""

    snet = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SocialNetworkPA(AbstractSocialNetwork):
    """social network profile association"""

    snet = models.ForeignKey(ProfileCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SocialNetworkPC(AbstractSocialNetwork):
    """social network profile company"""

    snet = models.ForeignKey(ProfileCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
