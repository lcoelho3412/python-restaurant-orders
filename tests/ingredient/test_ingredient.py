from src.models.ingredient import Ingredient, Restriction


# Req 1
def test_ingredient():
    ingredient_name = "presunto"
    ingredient2_name = "presunto"
    ingredient3_name = "salmão"

    ingredient = Ingredient(ingredient_name)
    ingredient2 = Ingredient(ingredient2_name)
    ingredient3 = Ingredient(ingredient3_name)

    assert ingredient.name == ingredient_name
    assert repr(ingredient) == f"Ingredient('{ingredient_name}')"

    assert hash(ingredient) == hash(ingredient2)
    assert hash(ingredient) != hash(ingredient3)
    assert ingredient == ingredient2
    assert ingredient != ingredient3

    assert ingredient.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
