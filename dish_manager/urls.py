from django.urls import path
from .views import (
    index,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishDeleteView,
    DishUpdateView,
    AssignNewView,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    IngredientListView,
    IngredientDetailView,
    IngredientCreateView,
    IngredientDeleteView,
    IngredientUpdateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dish/<int:dish_id>/assign/", AssignNewView.as_view(), name="dish-assign"),
    path("Ingredient/", IngredientListView.as_view(), name="ingredient-list"),
    path(
        "Ingredient/<int:pk>/", IngredientDetailView.as_view(), name="ingredient-detail"
    ),
    path(
        "Ingredient/create/",
        IngredientCreateView.as_view(),
        name="ingredient-create",
    ),
    path(
        "Ingredient/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient-update",
    ),
    path(
        "Ingredient/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient-delete",
    ),
    path("dishtype/", DishTypeListView.as_view(), name="dishtype-list"),
    path("dishtype/<int:pk>/", DishTypeDetailView.as_view(), name="dishtype-detail"),
    path("dishtype/create/", DishTypeCreateView.as_view(), name="dishtype-create"),
    path(
        "dishtype/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dishtype-update",
    ),
    path(
        "dishtype/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dishtype-delete",
    ),
]

app_name = "dish_manager"
