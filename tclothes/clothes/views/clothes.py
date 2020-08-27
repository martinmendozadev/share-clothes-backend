"""Clothes views."""

# Django REST Framework
from rest_framework import viewsets, mixins, status, serializers
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

# Interactions
from tclothes.clothes.views.interactions import Interactions


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
    ordering = ['-super_likes', '-likes']
    filter_fields = ['brand']

    @action(detail=False, methods=['POST', 'PUT'])
    def interactions(self, request, *args, **kwargs):
        user = request.user
        method = request.method
        match_obj = InteractionsModel.objects.filter(user=user, clothe_id=request.data['clothe'])
        if method == 'POST':
            match = InteractionsModel.objects.filter(user=user, clothe_id=request.data['clothe']).count()
            if match > 0:
                raise serializers.ValidationError(f'Use PUT, User its already a interaction with this clothe.')

        serializer = InteractionsModelSerializer(
            data=request.data,
            partial=False
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

        # Update stats clothe
        clothe = ClothesModel.objects.get(id=request.data['clothe'])
        user_action = request.data['value']
        interactions = Interactions(user_action, match_obj, clothe)
        if request.method == 'PUT':
            create_action = interactions.match_action
            create_action()

        if request.method == 'POST':
            create_action = interactions.create_action
            create_action()

        clothe.save()
        return Response(status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=['get'])
    def notifications(self, request, *args, **kwargs):
        """Retrieve notifications user matches."""
        user = request.user
        query = InteractionsModel.objects.filter(clothe__owner_is=user, value__in=['LIKE', 'SUPERLIKE'])
        data = NotificationsModelSerializer(query, many=True).data
        return Response(data, status=status.HTTP_200_OK)
