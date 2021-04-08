from rest_framework import serializers
from core.like import Like

# from users.serializers import UserPublicSerializer
# from campaings.header.serializers import CHDetailSerializer


class LikeSerializer(serializers.ModelSerializer):
    """like serializer"""

    class Meta:
        model = Like
        fields = ("liked",)
        read_only_fields = ("id",)
