from lib.menu import Menu
from lib.order import Order

"""
An instance of menu is initialized and the prop can be accessed
"""


def test_constructs_instance_of_menu_with_menu_prop():
    menu = Menu()
    order = Order(menu)

    assert order.menu == [
        {"item_number": 1, "item": "Pepperoni Pizza", "price": "9.99"},
        {"item_number": 2, "item": "American Hot", "price": "11.99"},
        {"item_number": 3, "item": "Margarita", "price": "8.99"},
    ]

