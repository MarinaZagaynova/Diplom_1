from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_available_buns(self, database_conf):
        assert len(database_conf.available_buns()) == 3

    def test_available_ingredients(self, database_conf):
        assert len(database_conf.available_ingredients()) == 6

    def test_quantity_available_fillings(self, database_conf):
        for ingredient in database_conf.available_ingredients():
            assert ingredient.get_type() in [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
