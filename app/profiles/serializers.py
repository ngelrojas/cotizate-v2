from rest_framework import serializers
from core.profile import PersonalProfile
from users.serializers import UserSerializer
from countries.serializers import CountrySerializer
from cities.serializers import CitySerializer


class PersonalSerializer(serializers.ModelSerializer):
    """model personal profile"""

    user = UserSerializer()
    countries = CountrySerializer()
    cities = CitySerializer()

    class Meta:
        model = PersonalProfile
        fields = "__all__"
