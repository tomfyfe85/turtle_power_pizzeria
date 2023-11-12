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
basket instance variable:
"""


def test_basket_is_updated_once_with_menu_item_1():
    menu = Menu()
    order = Order(menu)

    order.add_to_basket(1, 1)

    assert order.basket == [
        {"item_number": 1, "item": "Pepperoni Pizza", "price": "9.99"}
    ]


"""
Given valid parameters, Order#add_to_basket adds the multiple menu items of the same item number
to the basket instance variable
"""


def test_basket_is_updated_once_with_menu_item_2_3_times():
    menu = Menu()
    order = Order(menu)

    order.add_to_basket(2, 3)

    assert order.basket == [
        {"item_number": 2, "item": "American Hot", "price": "11.99"},
        {"item_number": 2, "item": "American Hot", "price": "11.99"},
        {"item_number": 2, "item": "American Hot", "price": "11.99"},
    ]


"""
Given valid parameters, Order#add_to_basket adds multiple different menu items to the
basket instance variable IE given add_to_basket(2, 1), add_to_basket(1, 2), add_to_basket(3, 3) :
"""


def test_basket_is_updated_multiple_times_with_multiple_menu_items():
    menu = Menu()
    order = Order(menu)
    order.add_to_basket(2, 1)
    order.add_to_basket(1, 2)
    order.add_to_basket(3, 3)


    assert order.basket == [
        {"item_number": 2, "item": "American Hot", "price": "11.99"},
        {"item_number": 1, "item": "Pepperoni Pizza", "price": "9.99"},
        {"item_number": 1, "item": "Pepperoni Pizza", "price": "9.99"},
        {"item_number": 3, "item": "Margarita", "price": "8.99"},
        {"item_number": 3, "item": "Margarita", "price": "8.99"},
        {"item_number": 3, "item": "Margarita", "price": "8.99"},
    ]


def test_add_to_basket_returns_confirmation_message():
    menu = Menu()
    order = Order(menu)

    menu.return_value = [
        {"item_number": 1, "item": "Pepperoni Pizza", "price": "9.99"},
        {"item_number": 2, "item": "American Hot", "price": "11.99"},
        {"item_number": 3, "item": "Margarita", "price": "8.99"},
    ]

    assert order.add_to_basket(2, 4) == "Your items have been add to the basket"


"""
Given a single order in the basket, Order#view_basket will return a formatted receipt of the item and the grand total
"""
def test_view_basket_returns_a_formatted_receipt_from_single_item():

    menu = Menu()
    order = Order(menu)
    
    order.add_to_basket(2, 1)
    assert order.view_basket() == "Your order:\n\n American Hot - £11.99\n\n Grand total: £11.99\n\n Thank you!"

