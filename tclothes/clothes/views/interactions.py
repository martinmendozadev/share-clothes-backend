"""Interactions methods"""

# Django REST framework
from rest_framework.serializers import ValidationError

# Models
from tclothes.users.models import Profile

# Utilities
from datetime import timedelta
from django.utils import timezone


class Interactions:
    """Interactions objects define logic of all interactions of application"""

    def __init__(self, user_action, clothe, user, interaction_obj=None):
        self.user_action = user_action
        self.clothe = clothe
        self.user = user
        self.user_profile = Profile.objects.get(user=self.user)
        self.interaction_obj = interaction_obj
        self.last_action_same_to_current = False
        self.like = 'LIKE'
        self.dislike = 'DISLIKE'
        self.super_like = 'SUPERLIKE'

    def update(self):
        """Lees the prev value from the clothe."""
        if self.interaction_obj.value != self.user_action:
            if self.interaction_obj.value == self.like:
                self.clothe.likes -= 1
            elif self.interaction_obj.value == self.super_like:
                self.clothe.super_likes -= 1
            elif self.interaction_obj.value == self.dislike:
                self.clothe.dislikes -= 1
            self.add_interaction()
        else:
            self.last_action_same_to_current = True

    def add_interaction(self):
        """Add the stats to clothe."""
        if self.user_action == self.like:
            self.clothe.likes += 1
        elif self.user_action == self.super_like:
            if self.verify_time():
                if not self.last_action_same_to_current:
                    self.clothe.super_likes += 1
                    self._update_last_super_like(self.user_profile)
        elif self.user_action == self.dislike:
            self.clothe.dislikes += 1
        self.clothe.save()

        if self.interaction_obj:
            self.interaction_obj.value = self.user_action
            self.interaction_obj.save()

    def verify_time(self):
        """Verify if user can do a super-like."""
        date_last_super_like = self.user_profile.last_super_like

        if date_last_super_like is not None:
            can_modify_at = date_last_super_like + timedelta(minutes=1)
            if timezone.now() > can_modify_at:
                return True
            raise ValidationError('Solo se puede dar un SUPER-LIKE por minuto.')
        return True

    @staticmethod
    def _update_last_super_like(profile):
        profile.last_super_like = timezone.now()
        profile.save()
