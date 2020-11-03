from django.db import models
from .abstract import AbstractProfile
from .profile import PersonalProfile
from .country import Country
from .city import City


class ProfileAssociation(AbstractProfile):
    """profile association"""

    representative_name = models.CharField(max_length=50)
    association_name = models.CharField(max_length=50)
    heading = models.CharField(max_length=50)
    email_company = models.EmailField(max_length=250, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    profiles = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE)
    countries = models.ForeignKey(Country, on_delete=models.CASCADE)
    cities = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.representative_name
