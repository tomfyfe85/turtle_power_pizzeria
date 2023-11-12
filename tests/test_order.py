from unittest.mock import Mock
from lib.order import Order

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
