from django.db import models
from .abstract import AbstractItem


class Category(AbstractItem):
    """category model"""

    imagen = models.CharField(max_length=1000, blank=True, null=True)
