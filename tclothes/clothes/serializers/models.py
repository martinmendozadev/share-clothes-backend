"""Clothes Model Serializer."""

# Django REST framework
from rest_framework import serializers

# Models
from tclothes.clothes.models import ClothesModel, InteractionsModel, ClothesPictureModel


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


class PictureClotheModelSerializer(serializers.ModelSerializer):
    """Pictures model serializer."""

    class Meta:
        """Meta class."""
        model = ClothesPictureModel
        fields = (
            'id',
            'clothe',
            'image',
        )


class ClotheModelSerializer(serializers.ModelSerializer):
    """Clothes model serializer."""

    more_pictures = PictureClotheModelSerializer(read_only=True)

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
            'more_pictures',
            'likes',
            'dislikes',
            'super_likes',
        )
        read_only_fields = ['id', 'limit_pictures', 'likes', 'dislikes', 'super_likes']
