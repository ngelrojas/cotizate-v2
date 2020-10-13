from core.reward import Reward


class RewardQuery:
    """query reward"""

    @staticmethod
    def get_list_reward(header_id):
        """get all list rewards about campaing header"""
        return Reward.objects.filter(header=header_id)

    @staticmethod
    def retrieve_reward(pk, header_id):
        """retrieve reward campaing header"""
        return Reward.objects.get(id=pk, header=header_id)
