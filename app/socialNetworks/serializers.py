from rest_framework import serializers
from core.socialNetwork import SocialNetworkPP
from core.socialNetwork import SocialNetworkPA
from core.socialNetwork import SocialNetworkPC
from profiles.serializers import PersonalSerializer
from profileCompanies.serializers import CompanySerializer


class SocialPPSerializer(serializers.ModelSerializer):
    """social network pp serializers"""

    snet = PersonalSerializer()

    class Meta:
        model = SocialNetworkPP
        fields = "__all__"


class SocialPASerializer(serializers.ModelSerializer):
    """social network pa serializers"""

    snet = CompanySerializer()

    class Meta:
        model = SocialNetworkPA
        fields = "__all__"


class SocialPCSerializer(serializers.ModelSerializer):
    """social network pc serializers"""

    snet = CompanySerializer()

    class Meta:
        model = SocialNetworkPC
        fields = "__all__"
