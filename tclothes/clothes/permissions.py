"""Clothes image permissions."""

# Django REST framework
from rest_framework.permissions import BasePermission
from rest_framework.serializers import ValidationError

# Models
from tclothes.clothes.models import ClothesModel


class IsClotheOwner(BasePermission):
    """Allow access only to objects owned by the requesting user."""

    def has_object_permission(self, request, view, obj):
        """Check obj and user are the same."""
        return request.user == obj.clothe.owner_is

    def has_permission(self, request, view):
        try:
            clothe = request.data['clothe']
            ClothesModel.objects.get(id=clothe, owner_is=request.user)
        except ClothesModel.DoesNotExist:
            return False
        except KeyError:
            raise ValidationError('Arguments are required.')
        return True
