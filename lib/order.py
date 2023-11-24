from lib.menu import Menu


class Order:
    def __init__(self, menu):
        # note .menu prop of the menu class = [dictionaries of menu items]
        # testing if an argument and the correct menu have been given.
        if menu is None:
            raise Exception("Error: Please enter the current menu")

        self.menu = menu.menu
        self.basket = []

    def add_to_basket(self, item_number, quantity):
        if item_number is None or item_number > 3 or item_number == 0 or quantity is None:
            raise Exception("Error: you must enter an valid item number and quantity")
        if quantity == 0:
            raise Exception("Error: quantity must be more than 0")

        for item in self.menu:
            if item["item_number"] == item_number:
                self.basket += quantity * [item]
        return "Your items have been add to the basket"

    # returns a formatted itemized receipt and a grand total
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
                return initial_string

    # def place_order(self, phone number):
    # confirm = Confirmation(phonenumber)
    # self.basket = []
    # return confirm.confirmation_text()
