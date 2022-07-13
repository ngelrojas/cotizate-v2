from django.db import models
from core.campaing import Campaing


class Phase(models.Model):
    """model phase"""

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=940)
    amount = models.DecimalField(max_digits=12, decimal_places=3)
    campaing = models.ForeignKey(Campaing, on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @classmethod
    def get_all(cls, campaing, delete=False):
        return cls.objects.filter(campaing=campaing, delete=delete) 

    @classmethod
    def get_phase(cls, campaing, pk, delete=False):
        retrieve = cls.objects.get(
                id=pk,
                campaing=campaing,
                delete=delete
        )
        return retrieve

    @classmethod
    def create(cls, campaing, request):
        created = cls.objects.create(
                title=request.data.get("title"),
                description=request.data.get("description"),
                campaing=campaing
        )
        return created.id

    @classmethod
    def update(cls, campaing, request, pk):
        updated = cls.get_phase(campaing, pk)
        updated.title = request.data.get("title")
        update.description = request.data.get("description")
        update.save()
        return updated.id

    @classmethod
    def erase(cls, campaing, pk):
        deleted = cls.get_phase(campaing, pk)
        deleted.delete = True
        deleted.save()
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
