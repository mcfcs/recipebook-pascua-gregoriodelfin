from datetime import datetime
from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Recipe(models.Model):
    pass

class RecipeIngredient(models.Model):
    pass
