from django.db import models
from core.campaing import CampaingHeader


class Upload(models.Model):
    """images table"""

    name = models.CharField(max_length=250)
    campaings = models.ForeignKey(CampaingHeader, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
