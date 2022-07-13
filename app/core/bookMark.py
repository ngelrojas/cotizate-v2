from django.db import models
from core.user import User
from core.campaing import Campaing


class BookMark(models.Model):
    """model like"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaing = models.ForeignKey(Campaing, on_delete=models.CASCADE)
    marked = models.BooleanField(default=False)

    def __str__(self):
        return self.campaing.title

    @classmethod
    def list_bookmark(cls, campaing, request):
        return cls.objects.filter(user=request.user, campaing=campaing)

    @classmethod
    def get_bookmark(cls, request, campaing, pk):
        bookmarked = cls.objects.get(
                id=pk,
                user=request.user,
                campaing=campaing
        )
        return bookmarked

    @classmethod
    def create(cls, request, campaing):
        created = cls.objects.create(
                user=request.user,
                campaing=campaing,
                marked=request.data.get("marked")
        )
        return created.id

    @classmethod
    def update(cls, campaing, request, pk):
        updated = cls.get_bookmark(campaing, pk)
        updated.marked = request.data.get("marked")
        updated.save()
        return updated.id
