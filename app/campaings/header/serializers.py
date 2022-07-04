from rest_framework import serializers
from core.campaing import Campaing
from cities.serializers import CitySerializer
from categories.serializers import CategorySerializer
from users.serializers import UserPublicSerializer

# from core.category import Category
# from core.city import City
# from users.serializers import UserSerializer
# from categories.serializers import CategorySerializer


class CampaingHeaderUp(serializers.ModelSerializer):
    """serializer for alterations"""

    class Meta:
        model = Campaing
        fields = (
            "id",
            "code_campaing",
        )


class CampaingHeaderSerializer(serializers.ModelSerializer):
    """campaing header serializer"""

    category = CategorySerializer()

    class Meta:
        model = Campaing
        fields = (
            "id",
            "user",
            "category",
            "city",
            "qty_day",
            "amount",
            "amount_reached",
            "percent_reached",
            "qty_day_left",
            "role",
            "code_campaing",
        )
        read_only_fields = ("id",)


class CHDetailSerializer(serializers.ModelSerializer):
    """campaing header serializer"""

    city = CitySerializer()
    category = CategorySerializer()
    user = UserPublicSerializer()

    class Meta:
        model = Campaing
        fields = (
            "id",
            "user",
            "category",
            "city",
            "qty_day_left",
            "amount",
            "amount_reached",
            "percent_reached",
            "role",
            "code_campaing",
        )
        read_only_fields = ("id",)
