from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Recipe, Category
from django.contrib.auth.models import User
from .test_recipe_base import RecipeTastBase


class RecipeViewsTest(RecipeTastBase):
    def tearDown(self) -> None:
        return super().tearDown()

    def test_recipe_home_view_funcao_se_correta(self):
        view = resolve(reverse('recipe:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_return_status_code_200_ok(self):
        response = self.client.get(reverse('recipe:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_carrega_templete_correto(self):
        response = self.client.get(reverse('recipe:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_tamplete_mostra_not_fond_se_nao_tem_receitas(self):
        Recipe.objects.all().delete()
        response = self.client.get(reverse('recipe:home'))
        self.assertIn(
            '<h4 class="alert-heading">Erro 404 - Página não encontrada!</h4>',
            response.content.decode('utf-8')
        )

    def test_recipe_home_tamplete_carrega_receitas(self):
        response = self.client.get(reverse('recipe:home'))
        response_content = response.content.decode('utf-8')
        response_context = response.context

        self.assertIn('Recipe Title', response_content)
        self.assertIn('10 minutos', response_content)
        self.assertIn('5 Porções', response_content)
        self.assertTrue('recipes' in response.context)
        self.assertEqual(len(response.context['recipes']), 1)

    def test_recipe_category_view_funcao_se_correta(self):
        view = resolve(reverse('recipe:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_return_status_404_se_nao_tem_receitas(self):
        response = self.client.get(
            reverse('recipe:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_funcao_se_correta(self):
        view = resolve(
            reverse('recipe:recipe', kwargs={'slug': 'peixe-frito'}))
        self.assertIs(view.func, views.recipe)

    def test_recipes_detail_view_return_status_404_se_nao_tem_receitas(self):
        Recipe.objects.all().delete()
        response = self.client.get(
            reverse('recipe:recipe', kwargs={'slug': 'recip-slug'}))
        self.assertEqual(response.status_code, 404)
