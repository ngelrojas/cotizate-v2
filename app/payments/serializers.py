from rest_framework import serializers
from core.payment import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """serializer payment model"""

    class Meta:
        model = Payment
        fields = ("__all__")
