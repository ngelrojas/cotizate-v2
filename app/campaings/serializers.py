from rest_framework import serializers
from core.campaing import Campaing
from cities.serializers import CitySerializer
from categories.serializers import CategorySerializer
from users.serializers import UserPublicSerializer


class CampaingSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    city = CitySerializer()
    user = UserPublicSerializer()

    class Meta:
        model = Campaing
        fields = "__all__"


