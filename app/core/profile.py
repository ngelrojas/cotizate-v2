from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .abstract import AbstractProfile
from .user import User


class PersonalProfile(AbstractProfile):
    """personal profile"""
    cellphone = models.CharField(max_length=20, blank=True, null=True)
    current_position = models.CharField(max_length=50, blank=True, null=True)
    current_city = models.CharField(max_length=45, blank=True, null=True)
    headline = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.first_name


@receiver(post_save, sender=User)
def personal_profile(sender, instance, created, **kwargs):
    if created:
        PersonalProfile.objects.create(user=instance)


class CompanyProfile(AbstractProfile):
    """company profile"""
    name = models.CharField(max_length=50, default='my company')
    phone = models.CharField(max_length=45, blank=True, null=True)
    cellphone = models.CharField(max_length=45, blank=True, null=True)
    email_company = models.EmailField(max_length=250, blank=True, null=True)
    represent = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
