from rest_framework import serializers
from core.bookMark import BookMark

# from users.serializers import UserPublicSerializer
# from campaings.header.serializers import CHDetailSerializer


class BookMarkSerializer(serializers.ModelSerializer):
    """bookmark serializer"""

    class Meta:
        model = BookMark
        fields = (
            "id",
            "marked",
        )
        read_only_fields = ("id",)
