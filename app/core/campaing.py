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

    # def get_not_del_and_archived(self, request):
    # """
    # get all campaing without deleted and archived
    # for current user
    # """
    # return Campaing.objects.filter(users=request.user).exclude(
    # Q(status=8) | Q(status=9)
    # )

    # @classmethod
    # def get_all_available(cls):
    # """get all available campaings to public"""
    # return Campaing.objects.filter(status=5)

    # @classmethod
    # def get_completed_campaings(cls):
    # """get all completed campaings to public"""
    # return Campaing.objects.filter(status=6)

    # @classmethod
    # def get_terminated_campaings(cls):
    # """get all completed campaings to public"""
    # return Campaing.objects.filter(status=7)

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
