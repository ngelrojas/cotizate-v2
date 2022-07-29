import datetime
from django.db import models
from django.utils import timezone
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
    delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @classmethod
    def get_all_campaings(cls, request):
        return cls.objects.filter(user=request.user, delete=False)

    @classmethod
    def get_by_category(cls, request, category):
        return cls.objects.filter(user=request.user, category=category, delete=False)

    @classmethod
    def get_by_city(cls, request, city):
        return cls.objects.filter(user=request.user, city=city, delete=False)

    @classmethod
    def get_by_status(cls, request, status):
        return cls.objects.filter(user=request.user, status=status, delete=False)

    @classmethod
    def get_by_flag(cls, request, flag):
        return cls.objects.filter(user=request.user, flag=flag, delete=False)

    @classmethod
    def get_by_role(cls, request, role):
        return cls.objects.filter(user=request.user, role=role, delete=False)

    @classmethod
    def get_campaing_id(cls, request, pk=None):
        return cls.objects.get(id=pk, user=request.user, delete=False)

    @classmethod
    def get_campaing_by_range_date_created(cls, request):
        return cls.objects.filter(
                        user=request.user,
                        created_at__range=[
                            request.data.get("date_created_at"),
                            request.data.get("date_ended_at")
                        ]
                )

    @classmethod
    def get_campaing_by_range_date_ended(cls, request):
        return cls.objects.filter(
                        user=request.user,
                        ended_at__range=[
                            request.data.get("date_created_at"),
                            request.data.get("date_ended_at")
                        ]
                )
    

    @classmethod
    def create(cls, objcate, objcity, objcurrency, request):
        created = cls.objects.create(
            title = request.data.get("title"), 
            video_main = request.data.get("video_main"), 
            imagen_main = request.data["imagen_main"], 
            excerpt = request.data.get("excerpt"), 
            description = request.data.get("description"),
            currency = objcurrency,  
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
        resp = cls.get_campaing_id(request, pk) 
        resp.title = request.data.get("title")
        if request.data.get("video_main"):
            resp.video_main = request.data.get("video_main")
        if request.data["imagen_main"]:
            resp.imagen_main = request.data["imagen_main"]
        resp.excerpt = request.data.get("excerpt")
        resp.description = request.data.get("description")
        resp.currency = objcurrency
        resp.short_url = request.data.get("short_url")
        resp.slogan_campaing = request.data.get("slogan_campaing")
        resp.category = objcate
        resp.city = objcity
        resp.updated_at = datetime.datetime.now(tz=timezone.utc) 
        resp.public_at = request.data.get("public_at")
        resp.ended_at = request.data.get("ended_at")
        resp.qty_day = request.data.get("qty_day")
        resp.qty_day_left = request.data.get("qty_day")
        resp.amount = request.data.get("amount")
        resp.role = request.data.get("role")
        resp.save()
        return resp.id


    @classmethod
    def erase(cls, request, pk):
        resp = cls.get_campaing_id(request, pk)
        resp.delete = True
        resp.save()
        return True

    @classmethod
    def get_all_campaings_by_status(cls, request, status):
        """TODO: continue query about campaings"""
        resp = cls.objects.filter(user=request.user, status=status, delete=False)
        return resp

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
