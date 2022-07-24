from django.db import models
from core.user import User
from core.campaing import Campaing


class Like(models.Model):
    """model like"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaing = models.ForeignKey(Campaing, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    @classmethod
    def get_all(cls, request):
        return cls.objects.filter(
                user=request.user,
                campaing=request.data.get("campaing_id")
        ) 

    @classmethod
    def get_like_by_id(cls, request, pk):
        resp = cls.objects.get(
                id=pk,
                user=request.user,
                campaing=request.data.get("campaing_id")
        )
        return resp

    @classmethod
    def created(cls, obj_campaing, request):
        resp = cls.objects.create(
                user=request.user,
                campaing=obj_campaing,
                liked = request.data.get("liked")
        )
        return resp.id

    @classmethod
    def updated(cls, request, pk):
        resp = cls.get_like_id(request, pk)
        resp.liked = request.data.get("liked")
        resp.save()
        return resp.id
