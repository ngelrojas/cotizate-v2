from datetime import datetime
from django.db import models
from autoslug import AutoSlugField
from core.user import User
from core.category import Category
from core.currency import Currency
from core.city import City


def nameFile(instance, filename):
    """save images in personal folder"""
    fdir = str(instance).replace(" ", "_")
    return "/".join(["images/campaings", fdir, filename])


class Campaing(models.Model):
    """model campaing body"""

    STATUS_CAMPAING = (
        (1, "created"),
        (2, "revised"),
        (3, "acepted"),
        (4, "public"),
        (5, "completed"),
        (6, "terminated"),
        (7, "archived"),
        (8, "deleted"),
    )

    FLAG_CAMPAING = (
        (1, "recent"),
        (2, "featured"),
        (3, "finished"),
    )

    ROLE_CAMPAING = ((1, "social cause"), (2, "entrepreneuship"))

    title = models.CharField(max_length=200)
    video_main = models.CharField(max_length=250, blank=True, null=True)
    imagen_main = models.ImageField(upload_to=nameFile)
    slug = AutoSlugField(populate_from="title", always_update=True)
    excerpt = models.CharField(max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    public_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CAMPAING, default=2)
    flag = models.PositiveSmallIntegerField(choices=FLAG_CAMPAING, default=1)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    short_url = models.CharField(max_length=100, null=True, blank=True)
    slogan_campaing = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    qty_day = models.IntegerField(default=0)
    qty_day_left = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    amount_reached = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    percent_reached = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    role = models.IntegerField(choices=ROLE_CAMPAING, default=2)
    code_campaing = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    @classmethod
    def get_all_campaings(cls, request, deleted=8):
        """get all campaings except deleted"""
        return Campaing.objects.exclude(user=request.user, status=deleted)

    @classmethod
    def get_campaing_id(cls, request, pk=None, status=8):
        """get campaing by id
            status = 8: deleted
        """
        return Campaing.objects.get(id=pk, user=request.user, status=status)

    @classmethod
    def create(cls, objcate, objcity, objcurrency, request):
        created = cls.objects.create(
            title = request.data.get("title"), 
            video_main = request.data.get("video_main"), 
            imagen_main = request.data["imagen_main"], 
            excerpt = request.data.get("excerpt"), 
            description = request.data.get("description"),
            currency = objcurrency  
            short_url = request.data.get("short_url"), 
            slogan_campaing = request.data.get("slogan_campaing"), 
            user = request.user, 
            category = objcate,
            city = objcity,
            qty_day = request.data.get("qty_day"), 
            qty_day_left = request.data.get("qty_day"), 
            amount = request.data.get("amount"),  
            role = request.data.get("role"),
            code_campaing = request.data.get("code_campaing") 
        )
        return created.id

    @classmethod
    def updated(cls, objcate, objcity, objcurrency, request, pk):
        updated = cls.get_campaing_id(request, pk) 
        update.title = request.data.get("title")
        if request.data.get("video_main"):
            update.video_main = request.data.get("video_main")
        if request.data["imagen_main"]:
            update.imagen_main = request.data["imagen_main"]
        update.excerpt = request.data.get("excerpt")
        update.description = request.data.get("description")
        update.currency = objcurrency
        update.short_url = request.data.get("short_url")
        update.slogan_campaing = request.data.get("slogan_campaing")
        update.category = objcate
        update.city = objcity
        update.updated_at = datetime.now()
        update.public_at = request.data.get("public_at")
        update.ended_at = request.data.get("ended_at")
        update.qty_day = request.data.get("qty_day")
        update.qty_day_left = request.data.get("qty_day")
        update.amount = request.data.get("amount")
        update.role = request.data.get("role")
        update.save()
        return updated.id


    @classmethod
    def deleted(cls, request, pk):
        erase = cls.get_campaing_id(request, pk)
        erase.status = 8
        erase.save()
        return True

    # def get_all_completed(self):
    # """get all completed campaing to
    # the current user
    # """
    # return Campaing.objects.filter(users=self.request.user, status=6)

    # def get_all_terminated(self):
    # """get all terminated campaing"""
    # return Campaing.objects.filter(users=self.request.user, status=7)

    # def get_archived(self, current_user):
    # """
    # get all archived campaing
    # current user
    # """
    # return Campaing.objects.filter(users=current_user, status=8)

    # def retrieve_campaing(self, current_user, pk):
    # """
    # retrieve current campaing with the current user
    # """
    # return Campaing.objects.exclude(Q(status=8) | Q(status=9)).get(
    # users=current_user, id=pk
    # )

    # def update_to_archived(self, current_user, pk):
    # """update status to archived=8"""
    # camp = Campaing.objects.exclude(
    # Q(status=9) | Q(status=5) | Q(status=6) | Q(status=7)
    # ).get(users=current_user, id=pk)
    # camp.status = 8
    # camp.save()
    # return camp

    # def update_to_delete(self, current_user, pk):
    # """update status to deleted=9"""
    # camp = Campaing.objects.exclude(
    # Q(status=5) | Q(status=6) | Q(status=7) | Q(status=8)
    # ).get(users=current_user, id=pk)
    # camp.status = 9
    # camp.save()
    # return camp
