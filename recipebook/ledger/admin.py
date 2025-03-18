"""
This module registers the models Recipe, RecipeIngredient, and Ingredient
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Recipe, RecipeIngredient, Ingredient, Profile

class IngredientAdmin(admin.ModelAdmin):
    """
    @brief Admin configuration for the Ingredient model.
    """
    list_display = ("id", "name")
    search_fields = ("name",)

class RecipeAdmin(admin.ModelAdmin):
    """
    @brief Admin configuration for the Recipe model.
    """
    list_display = ("id", "name")
    search_fields = ("name",)

class RecipeIngredientAdmin(admin.ModelAdmin):
    """
    @brief Admin configuration for the RecipeIngredient model.
    """
    list_display = ("id", "Recipe", "Ingredient", "Quantity")
    search_fields = ("Recipe__name", "Ingredient__name")
    list_filter = ("Recipe", "Ingredient")

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(admin.BaseUserAdmin):
    inlines = [ProfileInline,]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
