from django import forms
from .models import Recipe, RecipeImage

from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeImageForm(forms.ModelForm):
    """
    @brief Form for adding images to a Recipe.
    """
    class Meta:
        model = RecipeImage
        fields = '__all__'
