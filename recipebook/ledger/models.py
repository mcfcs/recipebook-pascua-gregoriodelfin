from datetime import datetime
from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Recipe(models.Model):
    name = models.CharField(max_length=100)

class RecipeIngredient(models.Model):
    pass
