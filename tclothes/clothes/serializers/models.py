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
        )
        read_only_fields = ['id', 'limit_pictures', 'likes', 'dislikes']
