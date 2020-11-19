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
