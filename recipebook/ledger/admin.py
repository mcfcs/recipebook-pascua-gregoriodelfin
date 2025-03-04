"""
This module registers the models Recipe, RecipeIngredient, and Ingredient
"""

from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient

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

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Ingredient, IngredientAdmin)
