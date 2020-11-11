from rest_framework import serializers
from core.profileCompany import ProfileCompany
from profiles.serializers import PersonalSerializer
from countries.serializers import CountrySerializer
from cities.serializers import CitySerializer


class CompanySerializer(serializers.ModelSerializer):
    """profile company serializer"""

    profiles = PersonalSerializer()

    class Meta:
        model = ProfileCompany
        fields = (
            "representative_name",
            "company_name",
            "representative",
            "association_name",
            "heading",
            "email_company",
            "photo",
            "profiles",
            "countries",
            "cities",
        )
        read_only_fields = ("id",)


class ProfileCompanySerializer(serializers.ModelSerializer):
    """profile company serializer without profiles"""

    countries = CountrySerializer()
    cities = CitySerializer()

    class Meta:
        model = ProfileCompany
        fields = (
            "representative_name",
            "company_name",
            "representative",
            "association_name",
            "heading",
            "email_company",
            "photo",
            "countries",
            "cities",
        )
        read_only_fields = ("id",)
