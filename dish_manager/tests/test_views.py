from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from dish_manager.models import DishType, Dish, Ingredient


class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.cook = get_user_model().objects.create_user(
            username="john_smith",
            first_name="John",
            last_name="Smith",
            password="Johns12345",
            years_of_experience=5,
        )
        self.dish_type = DishType.objects.create(name="Main Course")
        self.dish = Dish.objects.create(
            name="Pasta",
            description="Delicious pasta",
            price=12.99,
            dishtype=self.dish_type,
        )
        self.dish.cooks.add(self.cook)
        self.ingredient = Ingredient.objects.create(name="Tomato")
        self.ingredient.dishes.add(self.dish)

    def test_index_view(self):
        response = self.client.get(reverse("dish_manager:index"))
        self.assertEqual(response.status_code, 200)

    def test_cook_list_view(self):
        response = self.client.get(reverse("dish_manager:cook-list"))
        self.assertEqual(response.status_code, 200)

    def test_dish_list_view(self):
        response = self.client.get(reverse("dish_manager:dish-list"))
        self.assertEqual(response.status_code, 200)

    def test_dishtype_list_view(self):
        response = self.client.get(reverse("dish_manager:dishtype-list"))
        self.assertEqual(response.status_code, 200)

    def test_ingredient_list_view(self):
        response = self.client.get(reverse("dish_manager:ingredient-list"))
        self.assertEqual(response.status_code, 200)
