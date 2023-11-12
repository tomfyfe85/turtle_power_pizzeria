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
        initial_string = "Your order:\n\n"
        counter = 0
        final_cost = 0

        for item in self.basket:
            new_item = f" {item['item']} - £{item['price']}\n"

            initial_string += new_item
            final_cost += item["price"]
            counter += 1

            if counter == len(self.basket):
                initial_string += f"\n Grand total: £{final_cost}\n\n Thank you!"
                print(initial_string)
                return initial_string

