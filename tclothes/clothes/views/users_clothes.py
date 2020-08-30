"""Users Clothes views."""

# Django REST Framework
from rest_framework import viewsets, mixins, status, serializers
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated


# Models
from tclothes.clothes.models import ClothesModel
from tclothes.users.models import Profile

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

    def create(self, request, *args, **kwargs):
        """Create clothe."""
        serializer = ClotheModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_profile = Profile.objects.get(user=request.user)
        user_profile.remaining_clothes += 1
        if user_profile.remaining_clothes > 10:
            raise serializers.ValidationError('Solo puedes subir 10 prendas.')
        user_profile.save()
        clothe = serializer.save(owner_is=request.user)
        data = self.get_serializer(clothe).data
        return Response(data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        user_profile = Profile.objects.get(user=request.user)
        user_profile.remaining_clothes -= 1
        user_profile.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
