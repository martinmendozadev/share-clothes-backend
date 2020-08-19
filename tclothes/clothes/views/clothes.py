"""Clothes views."""

# Django REST Framework
from rest_framework import viewsets, mixins

# Permissions
from rest_framework.permissions import IsAuthenticated

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Models
from tclothes.clothes.models import ClothesModel

# Serializer
from tclothes.clothes.serializers import ClotheModelSerializer


class ClothesViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet,):
    """Clothes view set.
    Handle Clothes manage.
    """

    serializer_class = ClotheModelSerializer

    # Filters
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['size', '^color', '^category']
    ordering_fields = ['likes', 'size', 'gender', 'created_at']
    ordering = ['-likes']
    filter_fields = ['sell', 'is_hide']

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = ClothesModel.objects.all()
        if self.action == 'list':
            return queryset.filter(is_hide=False)
        return queryset

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]
