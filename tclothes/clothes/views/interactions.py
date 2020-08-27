"""Interactions methods"""

# Utilities
from datetime import timedelta
from django.utils import timezone
from rest_framework import serializers


class Interactions:
    """Interactions objects define logic of all interactions of application"""

    def __init__(self, user_action, interaction_obj, clothe):
        self.user_action = user_action
        self.interaction_obj = interaction_obj
        self.clothe = clothe

    def update(self):
        """Lees the prev value from the clothe."""
        try:
            match_current_value = self.interaction_obj[1].value
            if match_current_value != self.user_action:
                if match_current_value == 'LIKE':
                    self.clothe.likes -= 1
                elif match_current_value == 'SUPERLIKE':
                    self.clothe.super_likes -= 1
                elif match_current_value == 'DISLIKE':
                    self.clothe.dislikes -= 1

                self.create()
        except:
            raise serializers.ValidationError(f'Use POST, User has not interaction with this clothe.')

    def create(self):
        """Add some stat to the clothe."""
        if self.user_action == 'LIKE':
            self.clothe.likes += 1
        elif self.user_action == 'SUPERLIKE':
            can_modify_at = self.clothe.modified_at + timedelta(minutes=1)
            if timezone.now() > can_modify_at:
                self.clothe.super_likes += 1
            else:
                raise serializers.ValidationError('Sorry, you only can give one Super-like per minute.')
        else:
            self.clothe.dislikes += 1

        self.clothe.save()
