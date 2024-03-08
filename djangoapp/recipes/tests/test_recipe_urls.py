from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_recipe_home_url_verificando_se_correta(self):
        url = reverse('recipe:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_verificando_se_correta(self):
        url = reverse('recipe:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_recipe_url_verificando_se_correta(self):
        url = reverse('recipe:recipe', kwargs={'slug': 'peixe-frito'})
        self.assertEqual(url, '/recipes/peixe-frito/')
