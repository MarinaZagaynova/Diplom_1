from unittest.mock import patch, Mock

import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.data import name_bun, int_price, empty, float_price, name_souse, name_filling, ingredient_with_int_price, \
    ingredient_with_empty_name_and_float_price, ingredient_with_type_filling_and_float_price


class TestBurger:
    @pytest.mark.parametrize('name, price', [(name_bun, int_price), (empty, float_price)])
    def test_set_buns(self, burger_conf, name, price):
        bun = Bun(name, price)
        burger_conf.set_buns(bun)
        assert bun.get_name() == name and bun.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [(INGREDIENT_TYPE_SAUCE, name_souse, int_price),
                              (INGREDIENT_TYPE_SAUCE, empty, float_price),
                              (INGREDIENT_TYPE_FILLING, name_filling, float_price)])
    def test_add_ingredient(self, burger_conf, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        burger_conf.add_ingredient(ingredient)
        assert ingredient.get_name() == name and ingredient.get_price() == price and ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('index', [0, 1])
    def test_remove_ingredient(self, burger_conf, index):
        burger_conf.ingredients = [ingredient_with_int_price, ingredient_with_empty_name_and_float_price,
                                   ingredient_with_type_filling_and_float_price]
        burger_conf.remove_ingredient(index)
        assert len(burger_conf.ingredients) == 2

    def test_move_ingredient(self, burger_conf):
        burger_conf.ingredients = [ingredient_with_int_price, ingredient_with_empty_name_and_float_price,
                                   ingredient_with_type_filling_and_float_price]
        burger_conf.move_ingredient(1, 0)
        assert burger_conf.ingredients[0] == ingredient_with_empty_name_and_float_price

    def test_get_price(self, burger_conf):
        mock_ingredient = Mock(Ingredient)
        mock_ingredient.get_price.return_value = int_price
        mock_bun = Mock(Bun)
        mock_bun.get_price.return_value = float_price
        burger_conf.set_buns(mock_bun)
        burger_conf.add_ingredient(mock_ingredient)
        exp = float_price * 2 + int_price
        assert burger_conf.get_price() == exp

    @patch('praktikum.burger.Burger.get_price', return_value=101.1)
    def test_get_receipt(self, mock_burger_get_price, burger_conf):
        mock_ingredient = Mock(Ingredient)
        mock_ingredient.get_name.return_value = name_souse
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE

        mock_bun = Mock(Bun)
        mock_bun.get_name.return_value = name_bun
        burger_conf.set_buns(mock_bun)
        burger_conf.add_ingredient(mock_ingredient)

        assert str(burger_conf.get_receipt()) == ('(==== black bun ====)\n'
                                             '= sauce hot sauce =\n'
                                             '(==== black bun ====)\n'
                                             '\n'
                                             'Price: 101.1')

