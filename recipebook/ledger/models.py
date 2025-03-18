"""
@brief Models for Recipe app.
"""

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Bio = models.CharField(max_length=255)