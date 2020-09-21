from django.db import models
from .abstract import AbstractCC
from .country import Country


class City(AbstractCC):
    """country model"""

    countries = models.ForeignKey(Country, on_delete=models.CASCADE)
