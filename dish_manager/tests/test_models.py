from django.test import TestCase

from dish_manager.models import Cook, DishType, Dish, Ingredient


class CookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Cook.objects.create(
            username="john", first_name="John", last_name="Doe", years_of_experience=5
        )

    def test_cook_content(self):
        cook = Cook.objects.get(id=1)
        expected_object_name = f"{cook.username} ({cook.first_name} {cook.last_name})"
        self.assertEquals(expected_object_name, str(cook))


class DishTypeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        DishType.objects.create(name="Main Course")

    def test_dish_type_content(self):
        dish_type = DishType.objects.get(id=1)
        expected_object_name = dish_type.name
        self.assertEquals(expected_object_name, str(dish_type))


class DishModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        DishType.objects.create(name="Main Course")
        Cook.objects.create(
            username="john", first_name="John", last_name="Doe", years_of_experience=5
        )
        Dish.objects.create(
            name="Pasta",
            description="Delicious pasta",
            price=12.99,
            dishtype=DishType.objects.get(id=1),
        )

    def test_dish_content(self):
        dish = Dish.objects.get(id=1)
        expected_object_name = dish.name
        self.assertEquals(expected_object_name, str(dish))


class IngredientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Ingredient.objects.create(name="Tomato")

    def test_ingredient_content(self):
        ingredient = Ingredient.objects.get(id=1)
        expected_object_name = f"{ingredient.name} in {ingredient.dishes}"
        self.assertEquals(expected_object_name, str(ingredient))
