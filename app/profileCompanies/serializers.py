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
        fields = (
            "cinit",
            "address",
            "number_address",
            "neightbordhood",
            "cellphone",
            "telephone",
            "description",
            "complete",
            "rs_facebook",
            "rs_twitter",
            "rs_linkedin",
            "rs_another",
            "representative_name",
            "company_name",
            "representative",
            "association_name",
            "heading",
            "email_company",
            "photo",
            "user",
            "countries",
            "cities",
            "institution_type",
            "header",
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
