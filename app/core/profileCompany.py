from django.db import models
from .abstract import AbstractProfile
from .profile import PersonalProfile
from .country import Country
from .city import City
from .user import User


class ProfileCompany(AbstractProfile):
    """profile company"""

    TYPE_INST = ((1, "COMPANY"), (2, "ASSOCIATION"), (3, "ANOTHER"))
    representative_name = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    representative = models.BooleanField(default=False)
    association_name = models.CharField(max_length=50, blank=True, null=True)
    heading = models.CharField(max_length=50, blank=True, null=True)
    email_company = models.EmailField(max_length=250, blank=True, null=True)
    photo = models.TextField()
    profiles = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE)
    countries = models.ForeignKey(Country, on_delete=models.CASCADE)
    cities = models.ForeignKey(City, on_delete=models.CASCADE)
    institution_type = models.PositiveSmallIntegerField(choices=TYPE_INST, default=1)
    header = models.IntegerField(default=0)

    def __str__(self):
        return self.company_name
