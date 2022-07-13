from rest_framework import serializers
from core.bookMark import BookMark


class BookMarkSerializer(serializers.ModelSerializer):
    """bookmark serializer"""

    class Meta:
        model = BookMark
        fields = (
            "id",
            "marked",
        )
        read_only_fields = ("id",)
