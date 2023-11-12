from unittest.mock import Mock
from lib.order import Order

"""
Order#add_to_basket will return a nice message confirming the order has been placed
"""


def test_add_to_basket_returns_confirmation_message():
    menu = Mock()
    order = Order(menu)

    assert order.add_to_basket(2, 4) == "Your items have been add to the basket"
