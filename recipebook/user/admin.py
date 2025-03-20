"""
This module registers the Profile Model for the User
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    """
    @brief Instantiates Profile model to ProfileInline class.
    """
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    """
    @brief Instantiates ProfileInlines to UserAdmin class.
    """
    inlines = [ProfileInline,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
