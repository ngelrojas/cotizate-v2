from rest_framework import serializers
from core.profileAssociation import ProfileAssociation
from profiles.serializers import PersonalSerializer


class AssociationSerializer(serializers.ModelSerializer):
    """model profile association"""

    profile = PersonalSerializer()

    class Meta:
        model = ProfileAssociation
        fields = "__all__"
