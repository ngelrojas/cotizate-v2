from django.db import models


class Reward(models.Model):
    """model reward"""
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=12, decimal_places=3)
    campaings = models.IntegerField(default=0)
    users = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_all_reward(self, campaingId):
        return Reward.objects.filter(campaings=campaingId)

    def get_reward(self, rewardId):
        return Reward.objects.get(id=rewardId)

    def delete_reward(self, rewardId):
        return Reward.objects.get(id=rewardId).delete()
