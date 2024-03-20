from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from dish_manager.models import Cook, DishType, Dish


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user", password="admin12345"
        )
        self.client.force_login(self.admin_user)
        self.cook = Cook.objects.create_user(
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

    def test_cook_years_of_experience_listed(self):
        url = reverse("admin:dish_manager_cook_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_detailed_years_of_experience_listed(self):
        url = reverse("admin:dish_manager_cook_change", args=[self.cook.id])
        res = self.client.get(url)

        self.assertContains(res, self.cook.years_of_experience)
