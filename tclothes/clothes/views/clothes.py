"""Clothes views."""

# Django REST Framework
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action
from tclothes.clothes.serializers import InteractionsModelSerializer

# Permissions
from rest_framework.permissions import IsAuthenticated

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Models
from tclothes.clothes.models import ClothesModel, InteractionsModel

# Serializer
from tclothes.clothes.serializers import ClotheModelSerializer, NotificationsModelSerializer


class ClothesViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet,):
    """Clothes view set.
    Handle Clothes display.
    """

    serializer_class = ClotheModelSerializer
    queryset = ClothesModel.objects.filter(public=True)
    permission_classes = [IsAuthenticated]

    # Filters
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['size', '^color', '^category']
    ordering_fields = ['likes', 'size', 'gender', 'created_at']
    ordering = ['-likes']
    filter_fields = ['brand']

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

    @action(detail=False, methods=['get'])
    def notifications(self, request, *args, **kwargs):
        """Retrieve notifications user matches."""
        user = request.user
        query = InteractionsModel.objects.filter(user=user, value__in=['LIKE', 'SUPERLIKE'])
        data = NotificationsModelSerializer(query, many=True).data
        return Response(data, status=status.HTTP_200_OK)
