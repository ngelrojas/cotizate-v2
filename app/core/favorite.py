from django.db import models


class Favorite(models.Model):
    """model favorites"""

    users = models.IntegerField(default=0)
    campaings = models.IntegerField(default=0)

    def get_retrieve_favorite(self, pk):
        current_fav = Favorite.objects.get(id=pk)
        return current_fav
