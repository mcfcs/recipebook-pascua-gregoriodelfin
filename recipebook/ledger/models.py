"""
@brief Models for Recipe app.
"""

from django.db import models
from django.urls import reverse
from user.models import Profile

class Ingredient(models.Model):
    """
    @brief Instantiates Ingredient model.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.name)])

class Recipe(models.Model):
    """
    @brief Instantiates the Recipe model
    """
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.name)])

class RecipeIngredient(models.Model):
    """
    @brief Links Recipe & Ingredient Models.
    """
    Quantity = models.CharField(max_length=100)
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient")
    Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe")
