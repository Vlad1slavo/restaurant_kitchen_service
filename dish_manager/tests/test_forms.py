from django.test import TestCase
from django.contrib.auth import get_user_model
from dish_manager.forms import CookCreationForm, DishForm, CookUpdateForm

from dish_manager.models import DishType


class CookCreationFormTest(TestCase):
    def test_form_has_fields(self):
        form = CookCreationForm()
        expected = [
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "years_of_experience",
            "email",
        ]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)


class DishFormTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="john_smith",
            first_name="John",
            last_name="Smith",
            password="Johns12345",
            years_of_experience=5,
        )
        self.dish_type = DishType.objects.create(name="Main Course")

    def test_form_has_fields(self):
        form = DishForm()
        expected = ["name", "description", "price", "dishtype", "cooks"]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)


class CookUpdateFormTest(TestCase):
    def test_form_has_fields(self):
        form = CookUpdateForm()
        expected = ["first_name", "last_name", "years_of_experience", "email"]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)
