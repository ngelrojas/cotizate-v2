from django.test import TestCase
from core.reward import Reward


class RewardTests(TestCase):
    """test reward"""
    def test_create_reward(self):
        """create reward"""
        reward = Reward.objects.create(
            title='fist reward',
            description='first description',
            amount=88,
            campaings=1,
            users=0)
        self.assertEqual(reward.id, 1)
