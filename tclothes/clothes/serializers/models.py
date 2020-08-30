"""Clothes Model Serializer."""

# Django REST framework
from rest_framework import serializers

# Models
from tclothes.clothes.models import ClothesModel, InteractionsModel

# Foreign Serializers
from tclothes.users.serializers import UserDisplaySerializer


class InteractionsModelSerializer(serializers.ModelSerializer):
    """Interactions Model."""

    class Meta:
        model = InteractionsModel
        fields = ['value', 'clothe']
        required_fields = fields


class ClotheModelSerializer(serializers.ModelSerializer):
    """Clothes model serializer."""

    class Meta:
        """Meta class."""
        model = ClothesModel
        exclude = ['created_at', 'modified_at', 'owner_is']
        read_only_fields = ['id', 'clothe_images', 'likes', 'dislikes', 'super_likes']


class ClotheDisplaySerializer(serializers.ModelSerializer):
    """Clothes model serializer."""

    owner_is = UserDisplaySerializer(read_only=True)

    class Meta:
        """Meta class."""
        model = ClothesModel
        exclude = ['created_at', 'modified_at', 'dislikes', 'clothe_images', 'likes', 'super_likes']
        read_only_fields = ['id']


class NotificationsModelSerializer(serializers.ModelSerializer):
    """Interactions Model."""

    user = serializers.ReadOnlyField(read_only=True, source='user.username')
    clothe = ClotheModelSerializer(read_only=True)

    class Meta:
        model = InteractionsModel
        fields = ['clothe', 'user', 'value']
        read_only_fields = fields
