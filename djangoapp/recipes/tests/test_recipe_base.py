from django.test import TestCase
from recipes.models import Recipe, Category
from django.contrib.auth.models import User


class RecipeTastBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, name='Categoria'):
        return Category.objects.create(name=name)

    def make_author(
            self,
            first_name='firstname',
            last_name='lastname',
            username='username',
            password='123456',
            email='username@email.com',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_recipe(
            self,
            category_data=None,
            author_data=None,
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
    ):
        if category_data is None:
            category = {}

        if author_data is None:
            author = {}

        return Recipe.objects.create(
            category=self.make_category(**category),
            author=self.make_author(**author),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_step=preparation_step,
            preparation_step_is_html=preparation_step_is_html,
            is_published=is_published,
            cover=cover,
        )
