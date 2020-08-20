"""Users Clothes views."""

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
    Handle Users Clothes manage.
    """

    serializer_class = ClotheModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return all users clothes."""
        return ClothesModel.objects.filter(owner_is=self.request.user)
