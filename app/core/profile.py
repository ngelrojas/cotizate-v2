from django.db import models
from .abstract import AbstractProfile
from .user import User
from .country import Country
from .city import City


def user_directory_path(instance, filename):
    """personal-profile id"""
    return f"personalProfile/{instance.user.id}/{filename}"


class PersonalProfile(AbstractProfile):
    """personal profile"""

    current_position = models.CharField(max_length=50, blank=True, null=True)
    headline = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    photo = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    countries = models.ForeignKey(Country, on_delete=models.CASCADE)
    cities = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name
