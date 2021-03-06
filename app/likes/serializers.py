from rest_framework import serializers
from core.like import Like
from users.serializers import UserPublicSerializer
from campaings.header.serializers import CHDetailSerializer


class LikeSerializer(serializers.ModelSerializer):
    """like serializer"""

    user = UserPublicSerializer()
    header = CHDetailSerializer()

    class Meta:
        model = Like
        fields = (
            "id",
            "user",
            "header",
            "liked",
        )
        read_only_fields = ("id",)
