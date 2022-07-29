from django.db import models
from .abstract import AbstractItem


class Category(AbstractItem):
    """category model"""

    @classmethod 
    def list(cls, request, delete=False):
        return cls.object.filter(delete=delete)

    @classmethod
    def get_category(cls, pk, delete=False):
        resp = cls.objects.get(id=pk, delete=delete)
        return resp 

    @classmethod
    def create(cls, request):
        created = cls.objects.create(
                name=request.data.get("name"),
                description=request.data.get("description"),
                img_banner=request.data["img_banner"],
                img_icon=request.data["img_icon"]
        )
        return created.id

    @classmethod
    def update(cls, request, pk):
        updated = cls.get_category(id=pk)
        updated.name = request.data.get("name")
        updated.description = request.data.get("description")
        if request.data["img_banner"]:
            updated.img_banner = request.data["img_banner"]
        if request.data["img_icon"]:
            updated.img_icon = request.data["img_icon"]
        updated.save()
        return updated.id

    @classmethod
    def erase(cls, pk):
        deleted = cls.get_category(pk)
        deleted.delete = True
        deleted.save()
        return True

