from django.db import models
from .abstract import AbstractProfile
from .profile import PersonalProfile
from .country import Country
from .city import City


def user_directory_path(instance, filename):
    """personal-profile id"""
    return f"personalAssociation/{instance.PersonalProfile.id}/{filename}"


class ProfileAssociation(AbstractProfile):
    """profile association"""

    representative_name = models.CharField(max_length=50)
    association_name = models.CharField(max_length=50)
    heading = models.CharField(max_length=50)
    email_company = models.EmailField(max_length=250, blank=True, null=True)
    photo = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    profiles = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE)
    countries = models.ForeignKey(Country, on_delete=models.CASCADE)
    cities = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.representative_name