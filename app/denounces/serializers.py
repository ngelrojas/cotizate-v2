from rest_framework import serializers
from core.denounce import Denounce
from core.denounce import DenounceText


class DenounceSerializer(serializers.ModelSerializer):
    """denounce serializers"""

    class Meta:
        model = Denounce
        fields = "__all__"


class DenounceTextSerializer(serializers.ModelSerializer):
    """ deounce text serializers"""

    class Meta:
        model = DenounceText
        fields = "__all__"
