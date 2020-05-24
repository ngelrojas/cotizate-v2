from rest_framework import serializers
from core.currency import Currency


class CurrencySerializer(serializers.ModelSerializer):
    """currency serializers"""
    class Meta:
        model = Currency
        fields = ('name', 'symbol')
