"""Interactions methods"""

# Utilities
from datetime import timedelta
from django.utils import timezone

class Interactions:
    """Interactions objects define logic of all interactions of application"""
    def __init__(self, user_action, match_obj, clothe):
        self.user_action = user_action
        self.match_obj = user_action
        self.clothe = user_action
    
    def match_action(self):
        clothe = self.clothe
        user_action = self.user_action
        match_obj = self.match_obj

        try:
            match_current_value = match_obj[1].value
            if match_current_value != user_action:
                if match_current_value == 'LIKE':
                    clothe.likes -= 1
                elif match_current_value == 'SUPERLIKE':
                    clothe.super_likes -= 1
                elif match_current_value == 'DISLIKE':
                    clothe.dislikes -= 1
            
                self.create_action()
        except:
            raise serializers.ValidationError(f'Use POST, User has not interaction with this clothe.')
    
    def create_action(self):
        clothe = self.clothe
        user_action = self.user_action
    
        if user_action == 'LIKE':
            clothe.likes += 1
        elif user_action == 'SUPERLIKE':
            can_modify_at = clothe.modified_at + timedelta(minutes=1)
            if timezone.now() > can_modify_at:
                clothe.super_likes += 1
            else:
                raise serializers.ValidationError('Sorry, you only can give one Super-like per minute.')
        else:
            clothe.dislikes += 1