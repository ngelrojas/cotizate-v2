from rest_framework import serializers
from core.comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    """model comment serializer"""

    class Meta:
        model = Comment
        fields = ("id", "discuss", "campaings", "users", "parentid")
