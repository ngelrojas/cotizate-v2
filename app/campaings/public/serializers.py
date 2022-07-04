from rest_framework import serializers
from core.user import User
from core.campaing import Campaing
from cities.serializers import CitySerializer
from categories.serializers import CategorySerializer
from ..header.serializers import CHDetailSerializer
from profiles.serializers import PersonalSerializer


class CampaingPublicSerializer(serializers.ModelSerializer):
    """campaing public serializer"""

    header = CHDetailSerializer()

    class Meta:
        model = Campaing
        fields = (
            "id",
            "title",
            # "video_main",
            "imagen_main",
            "slug",
            "excerpt",
            # "description",
            # "created_at",
            # "updated_at",
            # "public_at",
            # "ended_at",
            # "status",
            "flag",
            "header",
            "currency",
            # "short_url",
            "slogan_campaing",
        )
        read_only_fields = ("id",)


class CampaingDetailSerializer(serializers.ModelSerializer):
    """campaing public serializer"""

    header = CHDetailSerializer()
    profile = PersonalSerializer()

    class Meta:
        model = Campaing
        fields = (
            "id",
            "title",
            "video_main",
            # "imagen_main",
            "slug",
            # "excerpt",
            "description",
            # "created_at",
            # "updated_at",
            "public_at",
            # "ended_at",
            "status",
            "flag",
            "header",
            "profile",
            "profile_ca",
            "currency",
            "short_url",
            "slogan_campaing",
        )
        read_only_fields = ("id",)
