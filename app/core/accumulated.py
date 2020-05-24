from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.campaing import Campaing
from core.payment import Payment


class Accumulated(models.Model):
    """model acumulated"""
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0)
    days_left = models.IntegerField(default=0)
    campaings = models.OneToOneField(
        Campaing,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.campaings.title


@receiver(post_save, sender=Campaing)
def create_accumulated(sender, instance, created, **kwargs):
    if created:
        Accumulated.objects.create(
            days_left=instance.qty_day,
            campaings=instance)


@receiver(post_save, sender=Payment)
def update_accumulated(sender, instance, **kwargs):
    caccumulated = Accumulated.objects.get(campaings=instance.campaings.id)
    caccumulated.amount = caccumulated.amount + instance.amount
    caccumulated.save()
