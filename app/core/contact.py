from django.db import models
from core.user import User


class Contact(models.Model):
    """
    contact table
    """

    from_user = models.IntegerField(default=0)
    to_user = models.IntegerField(default=0)
    description = models.CharField(max_length=600, default=0)
    first_name = models.CharField(max_length=255, default=0)
    last_name = models.CharField(max_length=255, default=0)
    email = models.EmailField(max_length=255, default=0)

    def __str__(self):
        return f"from {self.from_user} to {self.to_user}"
