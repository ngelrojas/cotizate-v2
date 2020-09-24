from rest_framework import serializers
from core.phase import Phase


class PhaseSerializer(serializers.ModelSerializer):
    """serialzier phase"""

    class Meta:
        model = Phase
        fields = "__all__"
