from rest_framework import serializers
from core.payment import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """serializer payment model"""

    class Meta:
        model = Payment
        fields = (
            "id",
            "name",
            "amount",
            "type_pay",
            "status_pay",
            "created_at",
            "users",
            "campaings",
        )
