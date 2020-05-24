from django.db import models
from autoslug import AutoSlugField


class AbstractProfile(models.Model):
    """abstract profile"""
    address = models.CharField(max_length=200, blank=True)
    dni = models.CharField(max_length=45, blank=True)
    country = models.CharField(max_length=45, blank=True)
    city = models.CharField(max_length=45, blank=True)
    complete = models.BooleanField(default=False)

    class Meta:
        abstract = True


class AbstractItem(models.Model):
    """abstract items like category and tag"""
    name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from='name', always_update=True)
    description = models.CharField(max_length=500)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
