from django.urls import reverse, resolve
from recipes import views
from recipes.models import Recipe
from .test_recipe_base import RecipeTastBase


class RecipeViewsTest(RecipeTastBase):
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
        response = self.client.get(reverse('recipe:home'))
        self.assertIn(
            '<h4 class="alert-heading">Erro 404 - Página não encontrada!</h4>',
            response.content.decode('utf-8')
        )

    def test_recipe_home_tamplete_carrega_receitas(self):
        # Cria uma receita
        self.make_recipe()
        # Carrega a página
        response = self.client.get(reverse('recipe:home'))
        # Decodifica o conteúdo da página
        response_content = response.content.decode('utf-8')
        response_context = response.context

        # Verifica se a receita foi carregada
        self.assertIn('Recipe Title', response_content)
        # Testes adicionais para aprender
        self.assertIn('10 minutos', response_content)
        self.assertIn('5 Porções', response_content)
        self.assertTrue('recipes' in response_context)
        self.assertEqual(len(response.context['recipes']), 1)

    def test_recipe_home_tamplete_nao_carrega_receitas_nao_publicadas(self):
        """
        Testa se a página home não carrega receitas não publicadas
        """
        self.make_recipe(is_published=False)
        # Carrega a página
        response = self.client.get(
            reverse('recipe:home'))
        # Decodifica o conteúdo da página
        response_content = response.content.decode('utf-8')
        # Verifica se a receita não foi carregada
        self.assertIn(
            '<h4 class="alert-heading">Erro 404 - Página não encontrada!</h4>',
            response.content.decode('utf-8')
        )

    def test_recipe_category_view_funcao_se_correta(self):
        view = resolve(reverse('recipe:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_return_status_404_se_nao_tem_receitas(self):
        response = self.client.get(
            reverse('recipe:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_tamplete_carrega_receitas(self):
        # Cria uma receita
        need_title = 'Title Category test'
        self.make_recipe(title=need_title)
        # Carrega a página
        response = self.client.get(reverse('recipe:category', args=(5,)))
        # Decodifica o conteúdo da página
        response_content = response.content.decode('utf-8')
        # Verifica se a receita foi carregada
        self.assertIn(need_title, response_content)

    def test_recipe_category_tamplete_nao_carrega_nao_publicado(self):
        """
            Testa se a página de categoria não carrega receitas não publicadas
        """
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse('recipe:category', kwargs={
                'category_id': recipe.category.id}))  # type: ignore
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_funcao_se_correta(self):
        view = resolve(
            reverse('recipe:recipe', kwargs={'slug': 'peixe-frito'}))
        self.assertIs(view.func, views.recipe)

    def test_recipes_detail_view_return_status_404_se_nao_tem_receitas(self):
        response = self.client.get(
            reverse('recipe:recipe', kwargs={'slug': 'recip-slug'}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_tamplete_carrega_receita_correta(self):
        # Cria uma receita
        need_title = 'Esta é página de detalhes da receita'
        self.make_recipe(title=need_title)
        # Carrega a página
        response = self.client.get(
            reverse('recipe:recipe', kwargs={'slug': 'recip-slug'}))
        # Decodifica o conteúdo da página
        response_content = response.content.decode('utf-8')
        # Verifica se a receita foi carregada
        self.assertIn(need_title, response_content)

    def test_recipe_datail_tamplete_nao_carrega_nao_publicado(self):
        """
            Testa se a página de detalhes da receita não carrega receitas não
            publicadas.
        """
        self.make_recipe(is_published=False)
        response = self.client.get(
            reverse('recipe:recipe', kwargs={'slug': 'recip-slug'}))
        self.assertEqual(response.status_code, 404)
