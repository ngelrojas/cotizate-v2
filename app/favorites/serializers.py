from rest_framework import serializers
from core.favorite import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    """favorite serializer"""

    class Meta:
        model = Favorite
        fields = (
            "id",
            "users",
            "campaings",
        )
        read_only_fields = ("id",)
