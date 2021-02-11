from django.db import models
from .abstract import AbstractItem
from .campaing import CampaingHeader

class Tag(AbstractItem):
    """category tag"""
    campaings = models.ForeignKey(CampaingHeader, on_delete=models.CASCADE)
