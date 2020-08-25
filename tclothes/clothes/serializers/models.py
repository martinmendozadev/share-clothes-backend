"""Clothes Model Serializer."""

# Django REST framework
from rest_framework import serializers

# Models
from tclothes.clothes.models import ClothesModel, InteractionsModel


class InteractionsModelSerializer(serializers.ModelSerializer):
    """Interactions Model."""

    class Meta:
        model = InteractionsModel
        fields = ('value', 'clothe')
        required_fields = fields


class NotificationsModelSerializer(serializers.ModelSerializer):
    """Interactions Model."""

    user = serializers.ReadOnlyField(read_only=True, source='user.username')

    class Meta:
        model = InteractionsModel
        fields = ['clothe', 'user', 'value']
        read_only_fields = fields


class ClotheModelSerializer(serializers.ModelSerializer):
    """Clothes model serializer."""

    class Meta:
        """Meta class."""
        model = ClothesModel
        fields = (
            'id',
            'picture',
            'limit_pictures',
            'description',
            'size',
            'color',
            'category',
            'gender',
            'brand',
            'state',
            'public',
            'likes',
            'dislikes',
            'super_likes',
        )
        read_only_fields = ['id', 'limit_pictures', 'likes', 'dislikes', 'super_likes']
