"""Clothes Model Serializer."""

# Django REST framework
from rest_framework import serializers

# Models
from tclothes.clothes.models import ClothesModel


class ClotheModelSerializer(serializers.ModelSerializer):
    """Clothes model serializer."""

    class Meta:
        """Meta class."""
        model = ClothesModel
        fields = (
            'id',
            'picture',
            'description',
            'size',
            'color',
            'category',
            'gender',
            'sell',
            'is_hide',
            'likes',
            'dislikes',
        )
        read_only_fields = ['id', 'likes', 'dislikes']
