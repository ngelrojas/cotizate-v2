from rest_framework import serializers
from core.comment import Comment
from users.serializers import UserPublicSerializer

class CommentSerializer(serializers.ModelSerializer):
    """model comment serializer"""
    users = UserPublicSerializer()
    
    class Meta:
        model = Comment
        fields = ("id", "discuss", "campaings", "users", "parentid")
