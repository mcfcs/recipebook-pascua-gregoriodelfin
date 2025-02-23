from django.urls import path
from . views import basicParams

urlpatterns = [
    path('', basicParams, name='basicParams'),
    path("recipe/<str:id>/", basicParams, name="basicParams"),
    path("recipes/list/", basicParams, name="basicParams")
]
