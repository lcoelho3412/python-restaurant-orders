from models.dish import Dish
from models.ingredient import Ingredient
import pandas as pd


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.data = pd.read_csv(source_path)

        dishes = {}
        for _, row in self.data.iterrows():
            name, price, ingredient, amount = row

            dish_data = dishes.get(name)
            if dish_data is None:
                dish_data = Dish(name, price)
                dishes[name] = dish_data
                self.dishes.add(dish_data)

            ingredient_data = Ingredient(ingredient)
            dish_data.add_ingredient_dependency(ingredient_data, amount)
