from rest_framework import serializers
from core.follower import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """follower serializer"""

    class Meta:
        model = Follower
        fields = "__all__"
        read_only_fields = ("id",)
