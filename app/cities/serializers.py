from rest_framework import serializers
from core.city import City
from countries.serializers import CountrySerializer


class CitySerializer(serializers.ModelSerializer):
    """country serializers"""

    countries = CountrySerializer()

    class Meta:
        model = City
        fields = (
            "id",
            "name",
            "slug",
            "short_name",
            "code_name",
            "description",
            "countries",
        )
