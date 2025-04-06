from django.urls import path
from .views import *

urlpatterns = [
    path("recipe/<int:pk>/", RecipeView.as_view(), name="recipe-detail"),
    path("recipes/list/", RecipeListView.as_view(), name="recipe-list"),
    path("recipe/add/", RecipeCreateView.as_view(), name="recipe-add"),
    path("recipe/<int:pk>/add_image", RecipeUpdateDetail.as_view(), name="recipe-add-image"),
]
