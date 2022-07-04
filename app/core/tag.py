from django.db import models
from .abstract import AbstractItem
from .campaing import Campaing


class Tag(AbstractItem):
    """category tag"""

    campaings = models.ForeignKey(Campaing, on_delete=models.CASCADE)
