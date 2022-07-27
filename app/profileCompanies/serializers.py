from rest_framework import serializers
from users.serializers import UserSerializer
from core.profileCompany import ProfileCompany
from countries.serializers import CountrySerializer
from cities.serializers import CitySerializer


class CompanySerializer(serializers.ModelSerializer):
    """profile company serializer"""

    user = UserSerializer()
    countries = CountrySerializer()
    cities = CitySerializer()

    class Meta:
        model = ProfileCompany
        fields = ("__all__")
        read_only_fields = ("id",)


class ProfileCompanySerializer(serializers.ModelSerializer):
    """profile company serializer without profiles"""

    countries = CountrySerializer()
    cities = CitySerializer()

    class Meta:
        model = ProfileCompany
        fields = (
            "representative",
            "company_name",
            "representative",
            "heading",
            "email_company",
            "photo",
            "countries",
            "cities",
        )
        read_only_fields = ("id",)
