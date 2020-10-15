from rest_framework import serializers
from core.campaing import CampaingHeader
from cities.serializers import CitySerializer
from categories.serializers import CategorySerializer

# from core.category import Category
# from core.city import City
# from users.serializers import UserSerializer
# from categories.serializers import CategorySerializer


class CampaingHeaderSerializer(serializers.ModelSerializer):
    """campaing header serializer"""

    class Meta:
        model = CampaingHeader
        fields = (
            "id",
            "user",
            "category",
            "city",
            "qty_day",
            "amount",
            "role",
            "code_campaing",
        )
        read_only_fields = ("id",)


class CHDetailSerializer(serializers.ModelSerializer):
    """campaing header serializer"""

    city = CitySerializer()
    category = CategorySerializer()

    class Meta:
        model = CampaingHeader
        fields = (
            "id",
            "user",
            "category",
            "city",
            "qty_day",
            "amount",
            "role",
            "code_campaing",
        )
        read_only_fields = ("id",)


# class CampaingPublicSerializer(serializers.ModelSerializer):
# """campaing serializer public"""

# users = UserSerializer()
# categories = CategorySerializer()
# tags = TagSerializer(many=True, read_only=True)
# currencies = CurrencySerializer()

# class Meta:
# model = Campaing
# fields = (
# "id",
# "title",
# "video_img",
# "slug",
# "excerpt",
# "description",
# "created_at",
# "updated_at",
# "public_at",
# "ended_at",
# "amount",
# "qty_day",
# "status",
# "users",
# "categories",
# "tags",
# "currencies",
# "profiles",
# )
