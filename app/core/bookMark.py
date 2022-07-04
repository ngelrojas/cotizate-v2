from django.db import models
from core.user import User
from core.campaing import Campaing


class BookMark(models.Model):
    """model like"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.ForeignKey(Campaing, on_delete=models.CASCADE)
    marked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name
