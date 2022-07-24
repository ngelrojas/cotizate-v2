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
    def list_bookmark(cls, request):
        return cls.objects.filter(user=request.user)

    @classmethod
    def get_bookmark(cls, request, pk):
        bookmarked = cls.objects.get(
                id=pk,
                user=request.user,
                campaing=request.data.get("campaing_id")
        )
        return bookmarked

    @classmethod
    def created(cls, request, campaing):
        resp = cls.objects.create(
                user=request.user,
                campaing=campaing,
                marked=request.data.get("marked")
        )
        return resp.id

    @classmethod
    def updated(cls, request, pk):
        resp = cls.get_bookmark(request, pk)
        resp.marked = request.data.get("marked")
        resp.save()
        return resp.id
