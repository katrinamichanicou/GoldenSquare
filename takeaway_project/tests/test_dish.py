from lib.dish import Dish
from unittest.mock import Mock
import pytest

"""
Given a name of a dish, it's price and number of units
check this is added to the dictionary
"""
def test_dish_creates_dict():
    dish_1 = Dish("Halloumi Fries", 5.5, 100)
    assert dish_1.dish == {
        "dish_name" : "Halloumi Fries",
        "dish_price" : 5.5,
        "availability" : 100
    }

"""
Given an instance of dish in format_dish
returns dish formatted as string
"""
def test_formatted_dish_returned():
    dish_1 = Dish("Halloumi Fries", 5.5, 100)
    assert dish_1.format_dish() == "Halloumi Fries ---- £5.5"

"""
Given a new price
The dish price is updated
"""
def test_price_updated_for_dish():
    dish_1 = Dish("Halloumi Fries", 5.5, 200)
    dish_1.update_price(7.5)
    assert dish_1.dish["dish_price"] == 7.5

# """
# Given an order instance is created (order placed)
# the number of units available
# for the instance of that dish is updated
# """
# def test_update_availability():
#     dish_1 = Dish("Halloumi Fries", 5.5, 200)
#     order_1 = Mock(name="order 1")
#     order_1.units_sold.return_value = 5
#     dish_1.update_availability(order_1)
#     assert dish_1.dish["availability"] == 195

"""
Given None/empty string or 0
raise exception to re-enter info
"""
