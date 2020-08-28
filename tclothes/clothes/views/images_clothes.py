"""Users Clothes views."""

# Django REST Framework
from rest_framework import viewsets, mixins

# Permissions
from rest_framework.permissions import IsAuthenticated
from tclothes.clothes.permissions import IsClotheOwner

# Models
from tclothes.clothes.models import ClothesPictureModel

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
