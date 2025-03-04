"""
This module registers the views of the django html
"""

from django.views.generic import ListView, DetailView
from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipehome.html'

class RecipeView(DetailView):
    model = Recipe
    template_name = 'recipe.html'
