"""
This module registers the models Recipe, RecipeIngredient, and Ingredient
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Recipe, RecipeIngredient, Ingredient, Profile

class RecipeAdmin(admin.ModelAdmin):
    """
    @brief Instantiates Recipe model to RecipeAdmin class.
    """
    model = Recipe

class RecipeIngredientAdmin(admin.ModelAdmin):
    """
    @brief Instantiates RecipeIngredient model to RecipeIngredientAdmin class.
    """
    model = RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    """
    @brief Instantiates Ingredient model to IngredientAdmin class.
    """
    model = Ingredient

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
