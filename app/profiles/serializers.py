from rest_framework import serializers
from core.profile import PersonalProfile
from users.serializers import UserSerializer


class PersonalSerializer(serializers.ModelSerializer):
    """model personal profile"""

    user = UserSerializer()

    class Meta:
        model = PersonalProfile
        fields = "__all__"
