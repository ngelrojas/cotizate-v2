from datetime import datetime
from django.db import models
from core.campaing import Campaing
from core.city import City


class Reward(models.Model):
    """model reward"""

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    expected_delivery = models.DateTimeField()
    campaing = models.ForeignKey(Campaing, on_delete=models.CASCADE)
    user = models.IntegerField(default=0)
    cities = models.ManyToManyField(City, blank=True)
    all_cities = models.BooleanField(default=False)
    pick_up_locally = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def list(cls, request, camp, erase=False):
        return cls.objects.filter(
                user=request.user,
                campaing=camp,
                delete=erase)

    @classmethod
    def get_reward(cls, request, camp, pk, erase=False):
        return cls.objects.get(
                id=pk,
                user=request.user,
                campaing=camp,
                delete=erase)

    @classmethod
    def create(cls, request, camp, objcity):
        created = cls.objects.create(
                title=request.data.get("title"),
                description=request.data.get("description"),
                amount=request.data.get("amount"),
                expected_delivery=request.data.get("expected_delivery"),
                campaing=camp,
                user=request.user,
                cities=objcity
        )
        return created.id

    @classmethod
    def updated(cls, request, camp, objcity):
        updated = cls.get_reward(request, camp, pk)
        update.title = request.data.get("title")
        update.description = request.data.get("description")
        update.amount = request.data.get("amount")
        update.expected_delivery = request.data.get("expected_delivery")
        update.cities = objcity
        update.update_at = datetime.now()
        update.save()
        return True

    @classmethod
    def erase(cls, request, camp, pk):
        delete = cls.get_reward(request, camp, pk)
        delete.delete = True
        delete.save()
        return True

#     def get_all_reward(self, request, campaingId):
# """private function"""
# return Reward.objects.filter(users=request.user.id, campaings=campaingId)

# def get_reward(self, rewardId, request):
# """private function"""
# return Reward.objects.get(users=request.user.id, id=rewardId)

# def delete_reward(self, request, rewardId):
# """private function"""
# return Reward.objects.get(users=request.user.id, id=rewardId).delete()

# def delete_all_reward(self, campaingID, request):
# return Reward.objects.filter(
# users=request.user.id, campaings=campaingID
# ).delete()

# def get_all_reward_public(self, campaingID):
# """
# public
# retrieve all reward about the current campaing"""
# return Reward.objects.filter(campaings=campaingID)
