from rest_framework import serializers
from core.upload import Upload


class UploadSerializer(serializers.ModelSerializer):
    """upload serializers"""

    class Meta:
        model = Upload
        fields = ("id", "name", "campaings")
