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
        """Interactions are ManyToOne but only users can have a unique interaction
        with whatever clothe for that reason need validate the atomic registers."""

        serializer = InteractionsModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        interaction_obj = None
        method = request.method
        user_action = request.data['value']
        clothe = ClothesModel.objects.get(id=request.data['clothe'])

        # Verify if interaction already exist.
        try:
            interaction_obj = InteractionsModel.objects.get(user=user, clothe_id=request.data['clothe'])
        except InteractionsModel.DoesNotExist:
            pass  # Dont worry for this :)

        # If action is POST when user dont have a Interaction with the clothe.
        if method == 'POST':
            if interaction_obj is None:
                interaction = Interactions(user_action, clothe, user)
                interaction.add_interaction()
                serializer.save(user=user)
            else:
                raise serializers.ValidationError('Use PUT | User have a previous interaction with this clothe.')

        # If actions is PUT go to update stats.
        if method == 'PUT':
            if interaction_obj is not None:
                interaction = Interactions(user_action, clothe, user, interaction_obj)
                interaction.update()
            else:
                raise serializers.ValidationError('Use POST | User dont have a previous interaction with this clothe.')

        return Response(status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=['get'])
    def notifications(self, request, *args, **kwargs):
        """Retrieve notifications user matches."""
        user = request.user
        query = InteractionsModel.objects.filter(clothe__owner_is=user, value__in=['LIKE', 'SUPERLIKE'])
        data = NotificationsModelSerializer(query, many=True).data
        return Response(data, status=status.HTTP_200_OK)
