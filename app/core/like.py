from django.db import models
from core.user import User
from core.campaing import CampaingHeader


class Like(models.Model):
    """model like"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.ForeignKey(CampaingHeader, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name
