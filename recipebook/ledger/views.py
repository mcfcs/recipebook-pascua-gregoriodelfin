"""
This module registers the views of the django html
"""

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipehome.html'
    redirect_field_name = "registration/login.html"

class RecipeView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'
    redirect_field_name = "registration/login.html"
