from rest_framework import serializers
from core.campaing import Campaing
from core.tag import Tag
from users.serializers import UserSerializer
from categories.serializers import CategorySerializer
from tags.serializers import TagSerializer
from currencies.serializers import CurrencySerializer


class CampaingSerializer(serializers.ModelSerializer):
    """campaing serializer"""
    users = UserSerializer()
    categories = CategorySerializer()
    tags = TagSerializer(many=True, read_only=True)
    currencies = CurrencySerializer()

    class Meta:
        model = Campaing
        fields = (
            'title',
            'slug',
            'excerpt',
            'description',
            'created_at',
            'updated_at',
            'public_at',
            'ended_at',
            'amount',
            'qty_day',
            'status',
            'users',
            'categories',
            'tags',
            'currencies')


class CCampaingSerializer(serializers.ModelSerializer):
    """campaing create serializer"""
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Campaing
        fields = (
            'title',
            'slug',
            'excerpt',
            'description',
            'created_at',
            'updated_at',
            'public_at',
            'ended_at',
            'amount',
            'qty_day',
            'status',
            'tags',
            'categories',
            'currencies')
        read_only_fields = ('id', )
