from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient

class IngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "Recipe", "Ingredient", "Quantity")
    search_fields = ("Recipe__name", "Ingredient__name")
    list_filter = ("Recipe", "Ingredient")

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Ingredient, IngredientAdmin)
