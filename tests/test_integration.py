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
Given valid parameters, Order#add_to_basket adds the appropriate menu items to the
basket instance variable IE given (1, 1):
basket == [{"item_number": 1, "item": "Pepperoni Pizza", "price": "9.99"}]
"""


def test_basket_is_updated_once_with_menu_item_1():
    menu = Menu()
    order = Order(menu)

    order.add_to_basket(1, 1)

    assert order.basket == [{"item_number": 1, "item": "Pepperoni Pizza", "price": "9.99"}]



def test_add_to_basket_returns_confirmation_message():
    menu = Menu()
    order = Order(menu)

    menu.return_value =  [
        {"item_number": 1, "item": "Pepperoni Pizza", "price": "9.99"},
        {"item_number": 2, "item": "American Hot", "price": "11.99"},
        {"item_number": 3, "item": "Margarita", "price": "8.99"},
    ]

    assert order.add_to_basket(2, 4) == "Your items have been add to the basket"
