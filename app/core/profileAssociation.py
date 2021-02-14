from django.db import models
from .abstract import AbstractProfile
from .profile import PersonalProfile
from .country import Country
from .city import City


class ProfileAssociation(AbstractProfile):
    """profile association"""

    representative_name = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    representative = models.BooleanField(default=False)
    association_name = models.CharField(max_length=50, blank=True, null=True)
    heading = models.CharField(max_length=50)
    email_company = models.EmailField(max_length=250, blank=True, null=True)
    # photo = models.ImageField(upload_to="associations/", blank=True, null=True)
    photo = models.CharField(max_length=250, blank=True, null=True)
    profiles = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE)
    countries = models.ForeignKey(Country, on_delete=models.CASCADE)
    cities = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.representative_name
