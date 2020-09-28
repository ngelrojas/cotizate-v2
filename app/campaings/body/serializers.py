from rest_framework import serializers
from core.campaing import CampaingBody

# from core.tag import Tag
# from users.serializers import UserSerializer
# from categories.serializers import CategorySerializer
# from tags.serializers import TagSerializer
# from currencies.serializers import CurrencySerializer


class CampaingBodySerializer(serializers.ModelSerializer):
    """campaing serializer"""

    # tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = CampaingBody
        fields = (
            "id",
            "title",
            "video_main",
            "imagen_main",
            "slug",
            "excerpt",
            "description",
            "created_at",
            "updated_at",
            "public_at",
            "ended_at",
            "status",
            "headers",
            "currency",
            "short_url",
            "slogan_campaing",
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
