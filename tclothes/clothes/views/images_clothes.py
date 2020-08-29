"""Users Clothes views."""

# Django REST Framework
from rest_framework import viewsets, mixins, status, serializers
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from tclothes.clothes.permissions import IsClotheOwner

# Models
from tclothes.clothes.models import ClothesPictureModel, ClothesModel

# Serializer
from tclothes.clothes.serializers import PictureClotheModelSerializer


class ClothesPicturesViewSet(mixins.CreateModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet,):
    """Clothes images view set.
    Handle Users Clothes images manage.
    """

    serializer_class = PictureClotheModelSerializer
    queryset = ClothesPictureModel.objects.all()
    permission_classes = [IsAuthenticated, IsClotheOwner]

    def create(self, request, *args, **kwargs):
        """Update clothes stats"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.clothe = ClothesModel.objects.get(id=request.data['clothe'], owner_is=request.user)
        self.clothe.clothe_images += 1
        if self.clothe.clothe_images == 3:
            raise serializers.ValidationError('Solo puedes subir 3 imagenes por prenda.')
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.clothe = ClothesModel.objects.get(id=request.data['clothe'], owner_is=request.user)
        self.clothe.clothe_images -= 1
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.save()
        self.clothe.save()

    def perform_destroy(self, instance):
        instance.delete()
        self.clothe.save()
