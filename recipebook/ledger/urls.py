from django.urls import path
from .views import *

urlpatterns = [
    path("recipe/<str:id>/", RecipeView.as_view(), name="recipe-detail"),
    path("recipes/list/", RecipeListView.as_view(), name="recipe-list")
]

