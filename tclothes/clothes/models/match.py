"""Match model"""

#Django
from django.db import models


class MatchModel(models.Model):
    """Match model"""

    id_clothe = models.ForeignKey(
        'id_clothe', 
        on_delete = models.CASCADE
    )

    id_user_like = models.ForeignKey(
        'users.User',
        on_delete = models.CASCADE
    )

    id_user_super_like = models.ForeignKey(
        'users.User',
        on_delete = models.CASCADE
    )

    id_user_dislike = models.ForeignKey(
        'users.User',
        on_delete = models.CASCADE
    )