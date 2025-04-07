import pytest
from random import choice, uniform

from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
from praktikum.burger import Burger

bun_list = ['Корочка хлеба', 'Коврига хлеба', 'Булочка с корицей', 'Сдобная булочка']
ingredient_0_sauce = ['Бешамель', 'Кепчуп', 'Гуакамоле']
ingredient_1_meat = ['Котлета', 'Жадина-говядина', 'Крабовая палочка']
ingredient_2_salad = ['Салат-латук', 'Маринованный лук', 'Крапива']
ingredient_3_cheese = ['Чеддер', 'Эмменталь', 'Бри']


@pytest.fixture()
def random_burger():
    bun = Bun(choice(bun_list), round(uniform(1, 100), 2))
    ingredient_0 = Ingredient('соус', choice(ingredient_0_sauce), round(uniform(1, 100), 2))
    ingredient_1 = Ingredient('мясо', choice(ingredient_1_meat), round(uniform(1, 100), 2))
    ingredient_2 = Ingredient('салат', choice(ingredient_2_salad), round(uniform(1, 100), 2))
    ingredient_3 = Ingredient('сыр', choice(ingredient_3_cheese), round(uniform(1, 100), 2))
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient_0)
    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)
    burger.add_ingredient(ingredient_3)
    return burger

@pytest.fixture()
def database():
    return Database()