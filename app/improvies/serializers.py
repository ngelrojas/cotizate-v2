from rest_framework import serializers
from core.improve import Improve


class ImproveSerializer(serializers.ModelSerializer):
    """serialzier phase"""

    class Meta:
        model = Improve
        fields = "__all__"
