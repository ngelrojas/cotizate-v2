from django.db import models
from .campaing import Campaing


class Updating(models.Model):
    """updating project"""

    header = models.ForeignKey(Campaing, on_delete=models.CASCADE)
    image_up = models.TextField()
    description = models.TextField()

    def __str__(self):
        return str(self.header.code_campaing)
