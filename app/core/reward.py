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

    def get_all_reward(self, request, campaingId):
        """private function"""
        return Reward.objects.filter(
            users=request.user.id,
            campaings=campaingId)

    def get_reward(self, rewardId, request):
        """private function"""
        return Reward.objects.get(users=request.user.id, id=rewardId)

    def delete_reward(self, request, rewardId):
        """private function"""
        return Reward.objects.get(
            users=request.user.id,
            id=rewardId).delete()

    def delete_all_reward(self, campaingID, request):
        return Reward.objects.filter(
            users=request.user.id,
            campaings=campaingID).delete()

    def get_all_reward_public(self, campaingID):
        """
        public
        retrieve all reward about the current campaing"""
        return Reward.objects.filter(campaings=campaingID)
