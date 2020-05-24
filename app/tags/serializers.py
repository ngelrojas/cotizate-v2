from rest_framework import serializers
from core.tag import Tag


class TagSerializer(serializers.ModelSerializer):
    """tag serializers"""

    class Meta:
        model = Tag
        fields = ("id", "name", "slug", "description")
