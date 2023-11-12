from unittest.mock import Mock
from lib.order import Order
import pytest


"""
Order#add_to_basket will return a nice message confirming the order has been placed
"""


def test_add_to_basket_returns_confirmation_message():
    menu = Mock(
        menu=[
            {"item_number": 1, "item": "Pepperoni Pizza", "price": 9.99},
            {"item_number": 2, "item": "American Hot", "price": 11.99},
            {"item_number": 3, "item": "Margarita", "price": 8.99},
        ]
    )
    order = Order(menu)
    assert order.add_to_basket(2, 4) == "Your items have been add to the basket"


"""
Raises error if menu.menu isn't the same as the menu in the Menu class
"""


def test_raises_error_the_wrong_menu_is_constructed():
    wrong_menu = Mock(
        menu=[
            {"item_number": 1, "item": "BBQ Chicken", "price": 9.99},
            {"item_number": 2, "item": "Hawaiian", "price": 11.99},
        ]
    )

    with pytest.raises(Exception) as e:
        order = Order(wrong_menu)
    err_msg = str(e.value)
    assert err_msg == "Error: Please enter the current menu"


"""
Order will throw error with no argument
"""


def test_throws_error_with_no_argument():
    with pytest.raises(Exception) as excinfo:
        order = Order(None)
    assert str(excinfo.value) == "Error: Please enter the current menu"


"""
NEXT 4 tests - Order#add_to_basket will throw an error if item_number, quantity, or 
item_number and quantity are missing and if quantity == 0
"""


def test_add_to_basket_throws_error_with_no_item_number():
    with pytest.raises(Exception) as e:
        menu = Mock(
            menu=[
                {"item_number": 1, "item": "Pepperoni Pizza", "price": 9.99},
                {"item_number": 2, "item": "American Hot", "price": 11.99},
                {"item_number": 3, "item": "Margarita", "price": 8.99},
            ]
        )
        order = Order(menu)
        order.add_to_basket(None, 1)
    assert str(e.value) == "Error: you must enter an valid item number and quantity"


def test_add_to_basket_throws_error_with_no_quantity():
    with pytest.raises(Exception) as e:
        menu = Mock(
            menu=[
                {"item_number": 1, "item": "Pepperoni Pizza", "price": 9.99},
                {"item_number": 2, "item": "American Hot", "price": 11.99},
                {"item_number": 3, "item": "Margarita", "price": 8.99},
            ]
        )
        order = Order(menu)
        order.add_to_basket(2, None)
    assert str(e.value) == "Error: you must enter an valid item number and quantity"


def test_add_to_basket_throws_error_with_no_arguments_given():
    with pytest.raises(Exception) as e:
        menu = Mock(
            menu=[
                {"item_number": 1, "item": "Pepperoni Pizza", "price": 9.99},
                {"item_number": 2, "item": "American Hot", "price": 11.99},
                {"item_number": 3, "item": "Margarita", "price": 8.99},
            ]
        )
        order = Order(menu)
        order.add_to_basket(None, None)
    assert str(e.value) == "Error: you must enter an valid item number and quantity"

def test_add_to_basket_throws_error_with_if_quantity_is_0():
    with pytest.raises(Exception) as e:
        menu = Mock(
            menu=[
                {"item_number": 1, "item": "Pepperoni Pizza", "price": 9.99},
                {"item_number": 2, "item": "American Hot", "price": 11.99},
                {"item_number": 3, "item": "Margarita", "price": 8.99},
            ]
        )
        order = Order(menu)
        order.add_to_basket(3, 0)
    assert str(e.value) == "Error: quantity must be more than 0"

"""
Order#add_to_basket will throw an error if item_number > 3
"""

def test_add_to_basket_throws_error_item_no_is_greater_than_no_of_items():
    with pytest.raises(Exception) as e:
        menu = Mock(
            menu=[
                {"item_number": 1, "item": "Pepperoni Pizza", "price": 9.99},
                {"item_number": 2, "item": "American Hot", "price": 11.99},
                {"item_number": 3, "item": "Margarita", "price": 8.99},
            ]
        )
        order = Order(menu)
        order.add_to_basket(4, 1)
    assert str(e.value) == "Error: you must enter an valid item number and quantity"

"""
Order#add_to_basket will throw an error if item_number == 0
"""

def test_add_to_basket_throws_error_item_no_is_0():
    with pytest.raises(Exception) as e:
        menu = Mock(
            menu=[
                {"item_number": 1, "item": "Pepperoni Pizza", "price": 9.99},
                {"item_number": 2, "item": "American Hot", "price": 11.99},
                {"item_number": 3, "item": "Margarita", "price": 8.99},
            ]
        )
        order = Order(menu)
        order.add_to_basket(0, 1)
    assert str(e.value) == "Error: you must enter an valid item number and quantity"

