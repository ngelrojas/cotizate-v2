from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.campaing import CampaingHeader
from core.payment import Payment


class Accumulated(models.Model):
    """model acumulated"""

    amount = models.DecimalField(max_digits=12, decimal_places=3, default=0)
    days_left = models.IntegerField(default=0)
    campaings = models.OneToOneField(CampaingHeader, on_delete=models.CASCADE)

    def __str__(self):
        return self.campaings.title
