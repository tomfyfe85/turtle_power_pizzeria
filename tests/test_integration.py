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


"""
Order#add_to_basket will return a nice message confirming the order has been placed
"""


def test_returns_confirmation_message():
    menu = Menu()
    order = Order(menu)

    assert order.add_to_basket(2, 4) == "Your items have been add to the basket"
