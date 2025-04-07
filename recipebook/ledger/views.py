"""
This module registers the views of the django html
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .models import Recipe
from .forms import RecipeForm, IngredientForm, RecipeIngredientForm, RecipeImageForm

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
    """
    @brief View for creating a recipe, an ingredient, and recipe-ingredient.
    """
    model = Recipe
    template_name = "recipeadd.html"
    form_class = RecipeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_form'] = kwargs.get('recipe_form') or self.get_form()
        context['ingredient_form'] = kwargs.get('ingredient_form') or IngredientForm()
        context['recipe_ingredient_form'] = kwargs.get('recipe_ingredient_form') or RecipeIngredientForm()
        return context

    def post(self, request, *args, **kwargs):
        recipe_form = RecipeForm(request.POST)
        ingredient_form = IngredientForm(request.POST)
        recipe_ingredient_form = RecipeIngredientForm(request.POST)

        if 'create_recipe' in request.POST and recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user.username
            recipe.save()
            return redirect('recipe-add')

        elif 'create_ingredient' in request.POST and ingredient_form.is_valid():
            ingredient_form.save()
            return redirect('recipe-add')

        elif 'create_recipe_ingredient' in request.POST and recipe_ingredient_form.is_valid():
            recipe_ingredient_form.save()
            return redirect('recipe-add')

        return render(request, self.template_name, {
            'recipe_form': recipe_form,
            'ingredient_form': ingredient_form,
            'recipe_ingredient_form': recipe_ingredient_form
        })

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
