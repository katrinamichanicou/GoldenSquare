from lib.order import Order
from lib.dish import Dish
from lib.menu import Menu
import pytest

"""
Given an instance of dish,
it is added to the Menu
"""
def test_dishes_added_to_dishes():
    dish_1 = Dish("Halloumi Fries", 5.5, 200)
    dish_2 = Dish("Halloumi & Cucumber Salad", 6, 100)
    dish_3 = Dish("Halloumi Feast", 11.5, 50)
    menu = Menu()
    menu.add_dish(dish_1)
    menu.add_dish(dish_2)
    menu.add_dish(dish_3)
    assert menu.dishes == [dish_1, dish_2, dish_3]

