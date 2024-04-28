from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

name_bun = "black bun"
empty = ""
int_price = 100
float_price = 101.10
name_souse = "hot sauce"
name_filling = "cutlet"
ingredient_with_int_price = Ingredient(INGREDIENT_TYPE_SAUCE, name_souse, int_price)
ingredient_with_empty_name_and_float_price = Ingredient(INGREDIENT_TYPE_SAUCE, empty, float_price)
ingredient_with_type_filling_and_float_price = Ingredient(INGREDIENT_TYPE_FILLING, name_filling, float_price)