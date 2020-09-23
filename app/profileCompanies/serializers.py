from rest_framework import serializers
from core.profileCompany import ProfileCompany
from profiles.serializers import PersonalSerializer


class CompanySerializer(serializers.ModelSerializer):
    """model profile association"""

    profile = PersonalSerializer()

    class Meta:
        model = ProfileCompany
        fields = "__all__"
