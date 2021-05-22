from rest_framework import serializers
from core.contact import Contact


class ContactSerializer(serializers.ModelSerializer):
    """denounce serializers"""

    class Meta:
        model = Contact
        fields = "__all__"
