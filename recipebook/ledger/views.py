"""
This module registers the views of the django html
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Recipe
from .forms import RecipeForm, RecipeImageForm

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

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipeadd.html"
    form_class = RecipeForm

    def get_success_url(self):
        return reverse_lazy('recipe-list', kwargs={'pk': self.object.pk})
    
class RecipeUpdateDetail(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = "recipeaddimage.html"
    form_class = RecipeImageForm

    def get_success_url(self):
        return reverse_lazy('recipe-detail', kwargs={'pk': self.get_object().pk})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = RecipeImageForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = Recipe.objects.get(pk = self.kwargs['pk'])
            recipe_image.save()
            return redirect(self.get_success_url())
        else:
            self.object_list = self.get_queryset(**kwargs)
            ctx = self.get_context_data(** kwargs)
            ctx['form'] = form
            return self.render_to_response(ctx)
