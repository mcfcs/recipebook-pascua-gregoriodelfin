from django.shortcuts import render
from django.views.generic import *
from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipehome.html'

class RecipeView(DetailView):
    model = Recipe
    template_name = 'recipe.html'