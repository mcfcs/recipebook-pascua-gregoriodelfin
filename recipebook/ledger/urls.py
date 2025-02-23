from django.urls import path
from . views import basic_params

urlpatterns = [
    path("recipe/<str:id>/", basic_params, name="basic_params"),
    path("recipes/list/", basic_params, name="basic_params")
]
