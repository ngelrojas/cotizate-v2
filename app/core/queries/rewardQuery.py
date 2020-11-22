from core.reward import Reward
from core.campaing import CampaingHeader


class RewardQuery:
    """query reward"""

    @staticmethod
    def get_list_reward(header_id):
        """get all list rewards about campaing header"""
        head_id = CampaingHeader.objects.get(id=header_id)
        return Reward.objects.filter(header=head_id)

    @staticmethod
    def retrieve_reward(pk, header_id):
        """retrieve reward campaing header"""
        return Reward.objects.get(id=pk, header=header_id)

    @classmethod
    def saving_rewards(cls, request):
        """
        saving rewards
        header"""
        try:
            header_id = CampaingHeader.objects.get(id=request.data.get("header"))
            rewards = Reward.objects.create(
                title=request.data.get("title"),
                description=request.data.get("description"),
                amount=request.data.get("amount"),
                expected_delivery=request.data.get("expected_delivery"),
                header=header_id,
                all_cities=request.data.get("all_cities"),
                pick_up_locally=request.data.get("pick_up_locally"),
            )
            for city in request.data.get("cities"):
                rewards.cities.add(city)

            return True
        except Exception:
            return False
