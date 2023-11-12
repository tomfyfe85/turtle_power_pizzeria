from lib.menu import Menu

"""
The menu should be initialized as a prop
"""


def test_the_menu_is_initialized():
    menu = Menu()

    assert menu.menu == [
        {"item_number": 1, "item": "Pepperoni Pizza", "price": 9.99},
        {"item_number": 2, "item": "American Hot", "price": 11.99},
        {"item_number": 3, "item": "Margarita", "price": 8.99},
    ]

"""
Given a menu is initialized, Menu#view should return a formatted version
Of the menu which is nice to read
"""

def test_view_returns_a_formatted_menu():

    menu = Menu()
    assert menu.view() == "Welcome to Tom's rad pizzeria!\n\n Menu:\n\n 1) Pepperoni - £9.99\n 2) American Hot - £11.99\n 3) Margarita - £8.99"

