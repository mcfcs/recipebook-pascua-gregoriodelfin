from django.shortcuts import render
from django.views.generic import *
from .models import Recipe

class TaskListView(ListView):
    model = Recipe
    template_name = 'recipehome.html'

class TaskDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'