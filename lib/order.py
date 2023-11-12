# from lib.menu import Menu


class Order:
    def __init__(self, menu):
        # note .menu prop of the menu class = [dictionaries of menu items]
        self.menu = menu.menu
        self.basket = []

    def add_to_basket(self, item_number, quantity ):

        for item in self.menu:
            if item["item_number"] == item_number:
              self.basket += quantity * [item]

        print(self.menu)      
        return "Your items have been add to the basket"