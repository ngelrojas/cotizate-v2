from django.db import models
from .abstract import AbstractCC
from .country import Country


class City(AbstractCC):
    """country model"""

    countries = models.ForeignKey(Country, on_delete=models.CASCADE)

    @classmethod
    def get_by_id(cls, id):
        return cls.objects.get(id=id, delete=False)
