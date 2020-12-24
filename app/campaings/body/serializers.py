from rest_framework import serializers
from core.campaing import CampaingBody

from profiles.serializers import PersonalSerializer
from campaings.header.serializers import CampaingHeaderSerializer

# from profileCompanies.serializers import ProfileCompanySerializer
from currencies.serializers import CurrencySerializer
from ..header.serializers import CHDetailSerializer


class CampaingBodySerializer(serializers.ModelSerializer):
    """campaing serializer"""

    header = CampaingHeaderSerializer()
    profile = PersonalSerializer()
    # profile_ca = ProfileCompanySerializer()
    currency = CurrencySerializer()

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
            "header",
            "profile",
            "profile_ca",
            "currency",
            "short_url",
            "slogan_campaing",
        )
        read_only_fields = ("id",)


class CampaingBodySearch(serializers.ModelSerializer):
    """campaing serializer"""

    header = serializers.IntegerField(write_only=True)
    profile = serializers.IntegerField(write_only=True)
    # profile_ca = ProfileCompanySerializer()
    currency = serializers.IntegerField(write_only=True)
    title = serializers.CharField(write_only=True)
    video_main = serializers.CharField(write_only=True)
    imagen_main = serializers.CharField(write_only=True)
    excerpt = serializers.CharField(write_only=True)
    description = serializers.CharField(write_only=True)
    created_at = serializers.CharField(write_only=True)

    updated_at = serializers.CharField(write_only=True)
    public_at = serializers.CharField(write_only=True)
    ended_at = serializers.CharField(write_only=True)
    status = serializers.CharField(write_only=True)
    profile_ca = serializers.CharField(write_only=True)
    short_url = serializers.CharField(write_only=True)
    slogan_campaing = serializers.CharField(write_only=True)

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
            "header",
            "profile",
            "profile_ca",
            "currency",
            "short_url",
            "slogan_campaing",
        )
        read_only_fields = ("id",)
