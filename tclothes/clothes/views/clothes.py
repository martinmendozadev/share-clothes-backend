"""Clothes views."""

# Django REST Framework
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from tclothes.clothes.permissions import IsClotheOwner

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
        if self.action in ['retrieve']:
            permissions = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthenticated, IsClotheOwner]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=True, methods=['get'])
    def myclothes(self, request, *args, **kwargs):
        """Update profile data."""
        user = request.user
        clothes = ClothesModel.objects.get(owner_is=user)
        data = ClotheModelSerializer(clothes).data
        return Response(data)
