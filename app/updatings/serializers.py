from rest_framework import serializers
from core.updating import Updating
from campaings.header.serializers import CampaingHeaderUp


class UpdatingSerializer(serializers.ModelSerializer):
    """updating serializers"""

    header = CampaingHeaderUp

    class Meta:
        model = Updating
        fields = ("id", "header", "image_up", "description")
