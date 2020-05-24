from rest_framework import serializers
from core.profile import CompanyProfile


class CompanySerializer(serializers.ModelSerializer):
    """serializer company profile"""
    name = serializers.CharField(max_length=50)
    dni = serializers.CharField(max_length=45)

    class Meta:
        model = CompanyProfile
        fields = (
            'name',
            'phone',
            'cellphone',
            'email_company',
            'address',
            'dni',
            'country',
            'city',
            'represent')
        extra_kwargs = {'complete': {'write_only': True}}
