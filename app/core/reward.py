from django.db import models
from core.campaing import Campaing
from core.city import City


class Reward(models.Model):
    """model reward"""

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    expected_delivery = models.DateTimeField()
    header = models.ForeignKey(Campaing, on_delete=models.CASCADE)
    user = models.IntegerField(default=0)
    cities = models.ManyToManyField(City, blank=True)
    all_cities = models.BooleanField(default=False)
    pick_up_locally = models.BooleanField(default=False)

    def __str__(self):
        return self.title


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
