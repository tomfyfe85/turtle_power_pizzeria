# from lib.menu import Menu


class Order:
    def __init__(self, menu):
        self.menu = menu.menu

    def add_to_basket(self, item_number, quantity ):
    # side effects: appends selected menu items to the list 
    # Returns:
    #   Message confirming the order is placed
        return "Your items have been add to the basket"