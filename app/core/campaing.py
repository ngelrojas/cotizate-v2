from django.db import models
from autoslug import AutoSlugField
from core.user import User
from core.category import Category
from core.currency import Currency
from core.city import City


def user_directory_path(instance, filename):
    """campaing id"""
    return f"campaing/{instance.user.id}/{filename}"


class CampaingHeader(models.Model):
    """model campaing header"""

    ROLE_CAMPAING = ((1, "social cause"), (2, "entrepreneuship"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    qty_day = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=12, decimal_places=3, default=0)
    role = models.IntegerField(choices=ROLE_CAMPAING, default=2)

    def __str__(self):
        return self.user.first_name


class CampaingBody(models.Model):
    """model campaing body"""

    STATUS_CAMPAING = (
        (1, "begin"),
        (2, "created"),
        (3, "revised"),
        (4, "acepted"),
        (5, "public"),
        (6, "completed"),
        (7, "terminated"),
        (8, "archived"),
        (9, "deleted"),
    )

    title = models.CharField(max_length=200)
    video_main = models.CharField(max_length=250)
    imagen_main = models.FileField(upload_to=user_directory_path)
    slug = AutoSlugField(populate_from="title", always_update=True)
    excerpt = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    public_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CAMPAING, default=2)
    header = models.ForeignKey(CampaingHeader, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    short_url = models.CharField(max_length=100, null=True, blank=True)
    slogan_campaing = models.CharField(max_length=200, null=True, blank=True)

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
