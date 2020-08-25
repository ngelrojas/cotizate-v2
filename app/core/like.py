from django.db import models


class Like(models.Model):
    """model like"""
    users = models.IntegerField(default=0)
    campaings = models.IntegerField(default=0)
    liked = models.BooleanField(default=False)

    def get_retrieve_like(self, request, pk):
        current_fav = Like.objects.get(
            users=request.user.id,
            id=pk)
        return current_fav
