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
        clothe = ClothesModel.objects.get(id=request.data['clothe'])
        user_action = request.data['value']
        interaction_obj = None

        # Validate input data
        serializer = InteractionsModelSerializer(
            data=request.data,
            partial=False
        )
        serializer.is_valid(raise_exception=True)

        # Verify if interaction already exist.
        try:
            interaction_obj = InteractionsModel.objects.get(user=user, clothe_id=request.data['clothe'])
        except InteractionsModel.DoesNotExist:
            pass

        # If action is POST. Create new Interaction object
        if method == 'POST':
            if interaction_obj is None:
                interaction = Interactions(user_action, clothe, True)
                interaction.create()
                serializer.save(user=user)
            else:
                raise serializers.ValidationError('Use PUT | POST-CLOTHES')

        # If actions is PUT go to update stats.
        if method == 'PUT':
            if interaction_obj is not None:
                print(interaction_obj.id)
                interaction = Interactions(user_action, clothe, False, interaction_obj)
                interaction.update()
            else:
                raise serializers.ValidationError(f'Use POST | PUT-CLOTHES.')

        return Response(status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=['get'])
    def notifications(self, request, *args, **kwargs):
        """Retrieve notifications user matches."""
        user = request.user
        query = InteractionsModel.objects.filter(clothe__owner_is=user)  # value__in=['LIKE', 'SUPERLIKE']
        data = NotificationsModelSerializer(query, many=True).data
        return Response(data, status=status.HTTP_200_OK)
