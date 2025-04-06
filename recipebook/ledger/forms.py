from django import forms
from .models import Recipe, RecipeImage

class RecipeForm(forms.ModelForm):
    """
    @brief Form for creating and editing Recipe.
    """
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeImageForm(forms.ModelForm):
    """
    @brief Form for adding images to a Recipe.
    """
    class Meta:
        model = RecipeImage
        fields = '__all__'
