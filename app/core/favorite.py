from django.db import models


class Favorite(models.Model):
    """model favorites"""
    users = models.IntegerField(default=0)
    campaings = models.IntegerField(default=0)

    def get_retrieve_favorite(self, request, pk):
        current_fav = Favorite.objects.get(
            users=request.user.id,
            id=pk)
        return current_fav
