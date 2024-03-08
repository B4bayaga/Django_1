from django.test import TestCase
from recipes.models import Recipe, Category
from django.contrib.auth.models import User


class RecipeTastBase(TestCase):
    def setUp(self) -> None:
        category = self.make_recipe()
        author = User.objects.create_user(
            first_name='firstname',
            last_name='lastname',
            username='username',
            password='123456',
            email='username@email.com',
        )
        self.recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe description',
            slug='recip-slug',
            preparation_time=10,
            preparation_time_unit='minutos',
            servings=5,
            servings_unit='Porções',
            preparation_step='Recipe preparation Step',
            preparation_step_is_html=False,
            is_published=True,
            cover='27/02/2024',
        )
        return super().setUp()

    def make_recipe(self):
        return Category.objects.create(name='Categoria')
