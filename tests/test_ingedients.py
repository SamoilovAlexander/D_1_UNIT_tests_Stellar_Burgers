import pytest

from datahelper import INGREDIENTS
from praktikum.ingredient import Ingredient


class TestIngredients:
    @pytest.mark.parametrize('ingredient_type, name, price', INGREDIENTS)
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, float(price))
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('ingredient_type, name, price', INGREDIENTS)
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, float(price))
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price', INGREDIENTS)
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, float(price))
        assert ingredient.get_price() == float(price)

