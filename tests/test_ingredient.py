import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.data import name_souse, empty, int_price, float_price, name_filling


def new_ingredient(ingredient_type, name, price):
    ingredient_conf = Ingredient(ingredient_type, name, price)
    return ingredient_conf


class TestIngredient:

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [(INGREDIENT_TYPE_SAUCE, name_souse, int_price), (INGREDIENT_TYPE_SAUCE, empty, float_price)])
    def test_get_name(self, ingredient_type, name, price):
        ingredient_name = new_ingredient(ingredient_type, name, price).get_name()
        assert ingredient_name == name

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [(INGREDIENT_TYPE_SAUCE, name_souse, int_price), (INGREDIENT_TYPE_SAUCE, empty, float_price)])
    def test_get_price(self, ingredient_type, name, price):
        ingredient_price = new_ingredient(ingredient_type, name, price).get_price()
        assert ingredient_price == price

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [(INGREDIENT_TYPE_SAUCE, name_souse, int_price),
                              (INGREDIENT_TYPE_FILLING, name_filling, float_price)])
    def test_get_type(self, ingredient_type, name, price):
        ingredient = new_ingredient(ingredient_type, name, price).get_type()
        assert ingredient == ingredient_type
