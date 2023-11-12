# from lib.menu import Menu


class Order:
    def __init__(self, menu):
        # note .menu prop of the menu class = [dictionaries of menu items]
        self.menu = menu.menu
        self.basket = []

    def add_to_basket(self, item_number, quantity):
        for item in self.menu:
            if item["item_number"] == item_number:
                self.basket += quantity * [item]
        return "Your items have been add to the basket"

    def view_basket(self):
        item = self.basket[0]
        result = f"Your order:\n\n {item['item']} - £{item['price']}\n\n Grand total: £{item['price']}\n\n Thank you!"
        print(item)
        print(result)
        return result  # returns an itemized list, formatted list of menu items and calculates the grand total
