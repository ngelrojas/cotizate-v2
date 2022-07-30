from django.db import models
from .abstract import AbstractItem


class Category(AbstractItem):
    """category model"""

    @classmethod 
    def get_all(cls, delete=False):
        return cls.object.filter(delete=delete)

    @classmethod
    def get_category(cls, pk, delete=False):
        resp = cls.objects.get(id=pk, delete=delete)
        return resp 

    @classmethod
    def created(cls, request):
        resp = cls.objects.create(
                name=request.data.get("name"),
                description=request.data.get("description"),
                img_banner=request.data["img_banner"],
                img_icon=request.data["img_icon"]
        )
        return resp.id

    @classmethod
    def updated(cls, request, pk):
        resp = cls.get_category(id=pk)
        resp.name = request.data.get("name")
        resp.description = request.data.get("description")
        if request.data["img_banner"]:
            resp.img_banner = request.data["img_banner"]
        if request.data["img_icon"]:
            resp.img_icon = request.data["img_icon"]
        resp.save()
        return resp.id

    @classmethod
    def erase(cls, pk):
        resp = cls.get_category(pk)
        resp.delete = True
        resp.save()
        return True

