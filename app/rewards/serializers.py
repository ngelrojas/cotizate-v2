from rest_framework import serializers
from core.reward import Reward


class RewardSerializer(serializers.ModelSerializer):
    """serialzier reward"""

    class Meta:
        model = Reward
        fields = "__all__"
