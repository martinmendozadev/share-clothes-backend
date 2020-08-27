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
        self.error_message = 'Use POST, interactions UPDATE.'

    def update(self):
        """Lees the prev value from the clothe."""
        try:
            current_value_interaction = self.interaction_obj[1].value
            if current_value_interaction != self.user_action:
                if current_value_interaction == 'LIKE':
                    self.clothe.likes -= 1
                elif current_value_interaction == 'SUPERLIKE':
                    if self.verify_time():
                        self.clothe.super_likes -= 1
                    else:
                        self.error_message = 'Solo se puede dar un superlike cada minuto. UPDATE'
                        raise serializers.ValidationError(self.error_message)
                elif current_value_interaction == 'DISLIKE':
                    self.clothe.dislikes -= 1

                self.clothe.save()
                self.create()
        except:
            raise serializers.ValidationError(self.error_message)

    def create(self):
        """Add the stat to the clothe."""
        if self.user_action == 'LIKE':
            self.clothe.likes += 1
        elif self.user_action == 'SUPERLIKE':
            if self.verify_time():
                self.clothe.super_likes += 1
            else:
                raise serializers.ValidationError('Solo se puede dar un superlike cada minuto. CREATE')
        elif self.user_action == 'DISLIKE':
            self.clothe.dislikes += 1

        self.clothe.save()

    def verify_time(self):
        """Verify if user can do a super-like."""
        can_modify_at = self.clothe.modified_at + timedelta(minutes=1)
        if timezone.now() > can_modify_at:
            return True
        return False
