from rest_framework import serializers
from core.campaing import CampaingHeader

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
            "qty_days",
            "amount",
            "role",
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
