from rest_framework import serializers
from core.profile import CompanyProfile


class CompanySerializer(serializers.ModelSerializer):
    """serializer company profile"""

    class Meta:
        model = CompanyProfile
        fields = (
            "id",
            "name",
            "phone",
            "cellphone",
            "email_company",
            "address",
            "dni",
            "country",
            "city",
            "represent",
        )
        extra_kwargs = {"complete": {"write_only": True}}
