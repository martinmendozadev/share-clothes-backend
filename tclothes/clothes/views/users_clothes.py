"""Clothes views."""

# Django REST Framework
from rest_framework import viewsets, mixins

# Permissions
from rest_framework.permissions import IsAuthenticated


# Models
from tclothes.clothes.models import ClothesModel

# Serializer
from tclothes.clothes.serializers import ClotheModelSerializer


class UsersClothesViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet,):
    """Clothes view set.
    Handle Clothes manage.
    """

    serializer_class = ClotheModelSerializer
    queryset = ClothesModel.objects.all()
    permission_classes = [IsAuthenticated]
