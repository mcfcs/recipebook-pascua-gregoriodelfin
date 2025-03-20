"""
@brief Models for User app.
"""

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    @brief Instantiates Profile model containing user, name, and bio.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)

    def __str__(self):
        return self.name
