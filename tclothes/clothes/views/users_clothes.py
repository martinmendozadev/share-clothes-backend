"""Users Clothes views."""

# Django REST Framework
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Permissions
from rest_framework.permissions import IsAuthenticated


# Models
from tclothes.clothes.models import ClothesModel

# Serializer
from tclothes.clothes.serializers import ClotheModelSerializer, InteractionsModelSerializer


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

        clothe = serializer.save(owner_is=request.user)
        data = self.get_serializer(clothe).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post', 'put'])
    def interactions(self, request, *args, **kwargs):
        user = request.user
        serializer = InteractionsModelSerializer(
            data=request.data,
            partial=False
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

        # Update stats clothe
        clothe = ClothesModel.objects.get(id=request.data['clothe'])
        user_action = request.data['value']
        if user_action == 'LIKE':
            clothe.likes += 1
        elif user_action == 'SUPERLIKE':
            clothe.likes += 10
        else:
            clothe.dislikes += 1
        clothe.save()

        return Response(status=status.HTTP_202_ACCEPTED)
