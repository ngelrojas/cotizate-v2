from rest_framework import serializers
from core.like import Like


class LikeSerializer(serializers.ModelSerializer):
    """like serializer"""

    class Meta:
        model = Like
        fields = (
            "id",
            "users",
            "campaings",
            "liked",
        )
        read_only_fields = ("id",)
