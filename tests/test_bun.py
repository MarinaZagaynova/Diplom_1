import pytest

from praktikum.bun import Bun
from tests.data import name_bun, int_price, empty, float_price


def add_bun(name, price):
    bun = Bun(name, price)
    return bun


class TestBun:

    @pytest.mark.parametrize('name, price', [(name_bun, int_price), (empty, float_price)])
    def test_get_name(self, name, price):
        bun = add_bun(name, price).get_name()
        assert bun == name

    @pytest.mark.parametrize('name, price', [(name_bun, int_price), (empty, float_price)])
    def test_get_price(self, name, price):
        bun = add_bun(name, price).get_price()
        assert bun == price
