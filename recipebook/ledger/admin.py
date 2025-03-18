"""
This module registers the models Recipe, RecipeIngredient, and Ingredient
"""

from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient

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

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Ingredient, IngredientAdmin)
