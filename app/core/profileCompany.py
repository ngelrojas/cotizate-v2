from django.db import models
from .abstract import AbstractProfile
from .profile import PersonalProfile


def user_directory_path(instance, filename):
    """personal-profile id"""
    return f"personalCompany/{instance.PersonalProfile.id}/{filename}"


class ProfileCompany(AbstractProfile):
    """profile company"""

    company_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    profiles = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name
