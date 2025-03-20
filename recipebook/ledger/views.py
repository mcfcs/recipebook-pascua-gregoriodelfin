"""
This module registers the views of the django html
"""

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

class RecipeListView(LoginRequiredMixin, ListView):
    """
    @brief Displays a list of all recipes
    accessible only to logged-in users.
    """
    model = Recipe
    template_name = 'recipehome.html'
    redirect_field_name = "registration/login.html"

class RecipeView(LoginRequiredMixin, DetailView):
    """
    @brief Displays detailed information about a single recipe
    accessible only to logged-in users.
    """
    model = Recipe
    template_name = 'recipe.html'
    redirect_field_name = "registration/login.html"
