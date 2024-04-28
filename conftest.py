import pytest

from praktikum.burger import Burger
from praktikum.database import Database


@pytest.fixture()
def burger_conf():
    burger_conf = Burger()
    return burger_conf


@pytest.fixture
def database_conf():
    database_conf = Database()
    return database_conf