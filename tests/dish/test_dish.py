from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish():
    with pytest.raises(TypeError):
        Dish("sushi", "cinquenta")

    with pytest.raises(ValueError):
        Dish("sushi", 0)

    dish_name = "sushi"
    dish2_name = "sushi"
    dish3_name = "strogonoff"
    dish_price = 50.00
    dish2_price = 50.00
    dish3_price = 20.00

    dish = Dish(dish_name, dish_price)
    dish2 = Dish(dish2_name, dish2_price)
    dish3 = Dish(dish3_name, dish3_price)

    assert dish.name == dish_name
    assert repr(dish) == f"Dish('{dish_name}', R${dish_price:.2f})"

    assert dish == dish2
    assert dish != dish3

    assert hash(dish) == hash(dish2)
    assert hash(dish) != hash(dish3)

    ingredient_name1 = "salmão"
    ingredient_name2 = "camarão"

    ingredient = Ingredient(ingredient_name1)
    ingredient2 = Ingredient(ingredient_name2)

    dish.add_ingredient_dependency(ingredient, 2)
    dish.add_ingredient_dependency(ingredient2, 1)

    assert dish.get_ingredients() == {
        Ingredient(ingredient_name1),
        Ingredient(ingredient_name2),
    }

    assert dish.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
