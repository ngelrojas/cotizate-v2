from rest_framework import serializers
from core.campaing import CampaingBody
from core.campaing import CampaingHeader

from profiles.serializers import PersonalSerializer

# from profileCompanies.serializers import ProfileCompanySerializer
from currencies.serializers import CurrencySerializer
from ..header.serializers import CHDetailSerializer


class CampaingBodySerializer(serializers.ModelSerializer):
    """campaing serializer"""

    header = CampaingHeader()
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
