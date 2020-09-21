from rest_framework import serializers
from core.country import Country


class CountrySerializer(serializers.ModelSerializer):
    """country serializers"""

    class Meta:
        model = Country
        fields = ("id", "name", "slug", "short_name", "code_name", "description")
