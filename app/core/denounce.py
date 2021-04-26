from django.db import models
from .campaing import CampaingHeader


class DenounceText(models.Model):
    """
    denounce text
    """

    title = models.CharField(max_length=300)
    description = models.CharField(max_length=600)

    def __str__(self):
        return self.title


class Denounce(models.Model):
    """
    denounce comments
    """

    marked = models.BooleanField(default=True)
    comment = models.CharField(max_length=500)
    denouncetxt = models.ForeignKey(DenounceText, on_delete=models.CASCADE)
    campaings = models.ForeignKey(CampaingHeader, on_delete=models.CASCADE)

    def __str__(self):
        return self.denouncetxt.title
