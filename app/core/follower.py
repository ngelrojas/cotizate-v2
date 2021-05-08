from django.db import models


class Follower(models.Model):
    """
    follower = current user
    following = campaing user
    status = True or False
    """

    follower = models.IntegerField()
    following = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.following)
