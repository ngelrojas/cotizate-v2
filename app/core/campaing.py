from django.db import models
from django.db.models import Q
from autoslug import AutoSlugField
from core.user import User
from core.category import Category
from core.tag import Tag
from core.currency import Currency


class Campaing(models.Model):
    """model campaing"""

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
    video_img = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from="title", always_update=True)
    excerpt = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    public_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=3, default=0)
    qty_day = models.PositiveSmallIntegerField(default=0)
    status = models.PositiveSmallIntegerField(choices=STATUS_CAMPAING, default=1)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    currencies = models.ForeignKey(Currency, on_delete=models.CASCADE)
    profiles = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_not_del_and_archived(self, request):
        """
        get all campaing without deleted and archived
        for current user
        """
        return Campaing.objects.filter(users=request.user).exclude(
            Q(status=8) | Q(status=9)
        )

    @classmethod
    def get_all_available(cls):
        """get all available campaings to public"""
        return Campaing.objects.filter(status=5)

    @classmethod
    def get_completed_campaings(cls):
        """get all completed campaings to public"""
        return Campaing.objects.filter(status=6)

    @classmethod
    def get_terminated_campaings(cls):
        """get all completed campaings to public"""
        return Campaing.objects.filter(status=7)

    def get_all_completed(self):
        """get all completed campaing to
        the current user
        """
        return Campaing.objects.filter(users=self.request.user, status=6)

    def get_all_terminated(self):
        """get all terminated campaing"""
        return Campaing.objects.filter(users=self.request.user, status=7)

    def get_archived(self, current_user):
        """
        get all archived campaing
        current user
        """
        return Campaing.objects.filter(users=current_user, status=8)

    def retrieve_campaing(self, current_user, pk):
        """
        retrieve current campaing with the current user
        """
        return Campaing.objects.exclude(Q(status=8) | Q(status=9)).get(
            users=current_user, id=pk
        )

    def update_to_archived(self, current_user, pk):
        """update status to archived=8"""
        camp = Campaing.objects.exclude(
            Q(status=9) | Q(status=5) | Q(status=6) | Q(status=7)
        ).get(users=current_user, id=pk)
        camp.status = 8
        camp.save()
        return camp

    def update_to_delete(self, current_user, pk):
        """update status to deleted=9"""
        camp = Campaing.objects.exclude(Q(status=5) | Q(status=6) | Q(status=7) | Q(status=8)).get(
            users=current_user, id=pk
        )
        camp.status = 9
        camp.save()
        return camp
