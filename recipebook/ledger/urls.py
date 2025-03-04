from django.urls import path
from .views import *

urlpatterns = [
    path("recipe/<int:pk>/", RecipeView.as_view(), name="recipe-detail"),
    path("recipes/list/", RecipeListView.as_view(), name="recipe-list")
]
