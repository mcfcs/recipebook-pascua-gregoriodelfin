"""
@brief Models for Recipe app.
"""

from django.db import models
from django.urls import reverse

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
    author = models.CharField(max_length=100)
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
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe")

    def __str__(self):
        return f"{self.recipe}: {self.ingredient} - {self.quantity}"
    
class RecipeImage(models.Model):
    """
    @brief Model for the recipe image.
    """

    image = models.ImageField(upload_to='images/', null=False)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="images")


