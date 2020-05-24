from rest_framework import serializers
from core.category import Category


class CategorySerializer(serializers.ModelSerializer):
    """category serializers"""
    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
            'description')
