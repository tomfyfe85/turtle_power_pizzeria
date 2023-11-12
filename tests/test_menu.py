from lib.menu import Menu

"""
The menu should be initialized as a prop
"""


def test_the_menu_is_initialized():
    menu = Menu()

    assert menu.menu == [
        {"item_number": 1, "item": "Pepperoni Pizza", "price": "9.99"},
        {"item_number": 2, "item": "American Hot", "price": "11.99"},
        {"item_number": 3, "item": "Margarita", "price": "8.99"},
    ]
