from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    with open(inventory_file_path, encoding="utf-8") as file:
        inventory_data = DictReader(file)
        inventory = {
            Ingredient(row["ingredient"]): int(row["initial_amount"])
            for row in inventory_data
        }
    return inventory


class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY):
        self.inventory = read_csv_inventory(inventory_file_path)

    def check_recipe_availability(self, recipe: Recipe) -> bool:
        for ingredient in recipe:
            if (
                ingredient not in self.inventory
                or int(recipe[ingredient]) > self.inventory[ingredient]
            ):
                return False
        return True

    def consume_recipe(self, recipe: Recipe) -> None:
        if not recipe:
            return None
        if not self.check_recipe_availability(recipe):
            raise ValueError
        for ingredient in recipe:
            self.inventory[ingredient] -= int(recipe[ingredient])
