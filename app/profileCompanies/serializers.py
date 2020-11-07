from rest_framework import serializers
from core.profileCompany import ProfileCompany
from users.serializers import UserSerializer
from profiles.serializers import PersonalSerializer


class CompanySerializer(serializers.ModelSerializer):
    """model profile association"""

    user = UserSerializer()

    class Meta:
        model = ProfileCompany
        fields = "__all__"
