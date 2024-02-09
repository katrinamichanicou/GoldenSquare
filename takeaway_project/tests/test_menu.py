from lib.menu import Menu
from unittest.mock import Mock

def test_menu_initially_empty_list():
    menu = Menu()
    assert menu.dishes == []

def test_dishes_added_to_menu():
    menu = Menu()
    dish_1 = Mock(name="dish 1")
    dish_2 = Mock(name="dish 2")
    menu.add_dish(dish_1)
    menu.add_dish(dish_2)
    assert menu.dishes == [dish_1, dish_2]

def test_dish_removed_from_menu():
    menu = Menu()
    dish_1 = Mock(name="dish 1")
    dish_2 = Mock(name="dish 2")
    menu.add_dish(dish_1)
    menu.add_dish(dish_2)
    menu.remove_dish(dish_2)
    assert menu.dishes == [dish_1]

