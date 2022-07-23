from datetime import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField
from core.user import User
from core.campaing import Campaing
from core.phase import Phase
from core.city import City


class Reward(models.Model):
    """model reward"""

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    expected_delivery = models.DateTimeField()
    campaing = models.ForeignKey(Campaing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    city = ArrayField(models.CharField(max_length=50)) 
    all_cities = models.BooleanField(default=False)
    pick_up_locally = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(null=True, blank=True)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @classmethod
    def get_all(cls, request, pk, erase=False):
        return cls.objects.filter(
                user=request.user,
                campaing=pk,
                delete=erase
        )

    @classmethod
    def get_reward(cls, request, pk, erase=False):
        return cls.objects.get(
                id=pk,
                user=request.user,
                campaing=request.data.get("campaing_id"),
                delete=erase)

    @classmethod
    def created(cls, request, obj_campaing, obj_phase):
        resp = cls.objects.create(
                title=request.data.get("title"),
                description=request.data.get("description"),
                amount=request.data.get("amount"),
                expected_delivery=request.data.get("expected_delivery"),
                campaing=obj_campaing,
                phase=obj_phase,
                city=request.data.get("city_id")
        )
        return resp.id

    @classmethod
    def updated(cls, request, pk):
        resp = cls.get_reward(request, pk)
        resp.title = request.data.get("title")
        resp.description = request.data.get("description")
        resp.amount = request.data.get("amount")
        resp.expected_delivery = request.data.get("expected_delivery")
        if request.data.get("city_id"):
            resp.cities = request.data.get("city_id") 
        resp.update_at = datetime.now().date()
        resp.phase = request.data.get("phase_id") 
        resp.campaing = request.data.get("campaing_id") 
        resp.save()
        return resp.id 

    @classmethod
    def erase(cls, request, pk):
        resp = cls.get_reward(request, pk)
        resp.delete = True
        resp.save()
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
