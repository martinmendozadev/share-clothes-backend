"""Clothes views."""

# Django REST Framework
from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.response import Response

# Serializer
from tclothes.clothes.serializers import (
    ClotheModelSerializer,
    CreateClotheSerializer
)


class ClothesViewSet(viewsets.GenericViewSet):
    """Clothes view set.
    Handle Clothes manage.
    """
    pass
