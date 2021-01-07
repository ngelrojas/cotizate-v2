from django.db import models
from autoslug import AutoSlugField


class AbstractProfile(models.Model):
    """abstract profile"""

    cinit = models.CharField(max_length=45)
    address = models.CharField(max_length=250)
    number_address = models.CharField(max_length=10)
    neightbordhood = models.CharField(max_length=250, blank=True)
    cellphone = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    rs_facebook = models.CharField(max_length=350, blank=True, null=True)
    rs_twitter = models.CharField(max_length=350, blank=True, null=True)
    rs_linkedin = models.CharField(max_length=350, blank=True, null=True)
    rs_another = models.CharField(max_length=350, blank=True, null=True)

    class Meta:
        abstract = True


class AbstractItem(models.Model):
    """abstract items like category and tag"""

    name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from="name", always_update=True)
    description = models.CharField(max_length=500)
    img_banner = models.ImageField(upload_to="banners/", blank=True, null=True)
    img_icon = models.ImageField(upload_to="icons/", blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class AbstractCC(models.Model):
    """abstract data for country and city"""

    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name", always_update=True)
    short_name = models.CharField(max_length=50, blank=True, null=True)
    code_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class AbstractSocialNetwork(models.Model):
    """abstract model for social network"""

    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        abstract = True
