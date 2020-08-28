"""Interactions methods"""

# Django REST framework
from rest_framework.serializers import ValidationError

# Utilities
from datetime import timedelta
from django.utils import timezone


class Interactions:
    """Interactions objects define logic of all interactions of application"""

    def __init__(self, user_action, clothe, is_new, interaction_obj=None):
        self.user_action = user_action
        self.clothe = clothe
        self.is_new = is_new
        self.interaction_obj = interaction_obj
        self.like = 'LIKE'
        self.dislike = 'DISLIKE'
        self.super_like = 'SUPERLIKE'

    def update(self):
        """Lees the prev value from the clothe."""
        if self.interaction_obj.value != self.user_action:
            if self.interaction_obj.value == self.like:
                self.clothe.likes -= 1
            elif self.interaction_obj.value == self.super_like:
                if self.verify_time():
                    self.clothe.super_likes -= 1
            elif self.interaction_obj.value == self.dislike:
                self.clothe.dislikes -= 1

            self.clothe.save()
            self.add_interaction()

    def add_interaction(self):
        """Add the stats to clothe."""
        if self.user_action == self.like:
            self.clothe.likes += 1
        elif self.user_action == self.super_like:
            if self.is_new:
                self.clothe.super_likes += 1
            else:
                if self.verify_time():
                    self.clothe.super_likes += 1
        elif self.user_action == self.dislike:
            self.clothe.dislikes += 1
        self.clothe.save()

        if not self.is_new:
            self.interaction_obj.value = self.user_action
            self.interaction_obj.save()

    def verify_time(self):
        """Verify if user can do a super-like."""
        can_modify_at = self.interaction_obj.modified_at + timedelta(minutes=1)
        if timezone.now() > can_modify_at:
            return True
        raise ValidationError('Solo se puede dar un SUPER-LIKE por minuto.')
