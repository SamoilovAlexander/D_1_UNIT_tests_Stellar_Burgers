import pytest

from datahelper import BUNS, INGREDIENTS
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
from praktikum.burger import Burger



class TestBurger:
    @pytest.mark.parametrize('name, price', BUNS)
    def test_set_buns(self, name, price):
        burger = Burger()
        bun = Bun(name, float(price))
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize('ingredient_type, name, price', INGREDIENTS)
    def test_add_ingredient(self, ingredient_type, name, price):
        burger = Burger()
        ingredient = Ingredient(ingredient_type, name, float(price))
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    @pytest.mark.parametrize('ingredient_type, name, price', INGREDIENTS)
    def test_remove_ingredient(self, ingredient_type, name, price):
        burger = Burger()
        ingredient = Ingredient(ingredient_type, name, float(price))
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, random_burger):
        random_burger.move_ingredient(3, 0)
        assert random_burger.ingredients[0].get_type() == 'сыр'

    def test_get_price(self, random_burger):
        price = random_burger.bun.get_price() * 2
        for i in random_burger.ingredients:
            price += i.get_price()
        assert random_burger.get_price() == price

    def test_get_receipt(self, random_burger):
        assert random_burger.bun.get_name() in random_burger.get_receipt() and random_burger.ingredients[0].get_name() in random_burger.get_receipt() and str(random_burger.get_price()) in random_burger.get_receipt()