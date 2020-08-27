from rest_framework import serializers
from core.profile import PersonalProfile


class PersonalSerializer(serializers.ModelSerializer):
    """model personal profile"""
    dni = serializers.CharField(max_length=45)
    birthdate = serializers.DateField()
    age = serializers.IntegerField()

    class Meta:
        model = PersonalProfile
        fields = (
            'address',
            'dni',
            'complete',
            'country',
            'city',
            'cellphone',
            'current_position',
            'current_city',
            'headline',
            'birthdate',
            'age')
