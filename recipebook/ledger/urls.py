from django.urls import path, include
from .views import *

urlpatterns = [
    path("recipe/<int:pk>/", RecipeView.as_view(), name="recipe-detail"),
    path("recipes/list/", RecipeListView.as_view(), name="recipe-list"),
    path('/accounts', include('django.contrib.auth.urls'))
]
