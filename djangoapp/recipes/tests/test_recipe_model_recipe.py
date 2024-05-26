from .test_recipe_base import RecipeTastBase
from django.core.exceptions import ValidationError
from parameterized import parameterized


# Define uma classe de teste para o modelo de receita
class RecipeModelTest(RecipeTastBase):
    # Método setUp é executado antes de cada teste
    def setUp(self) -> None:
        # Cria uma nova receita usando o método make_recipe
        self.recipe = self.make_recipe()
        # Chama o método setUp da classe base
        return super().setUp()
            
    # Usa o decorador parameterized.expand para parametrizar o teste
    @parameterized.expand([
            # Cada tupla representa um conjunto diferente de parâmetros para o teste
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ])
    # Define o método de teste
    def test_recipe_max_length(self,fild, max_length):
        # Define o valor do campo para uma string que é uma vez mais longa que o comprimento máximo
        setattr(self.recipe, fild, 'a' * (max_length + 1))
        # Espera que uma ValidationError seja lançada quando full_clean é chamado
        with self.assertRaises(ValidationError) as cm: 
            # Método que é responsável por validar os dados do objeto
            self.recipe.full_clean()
