class Menu:
    def __init__(self):
        self.menu = [
            {"item_number": 1, "item": "Pepperoni Pizza", "price": 9.99},
            {"item_number": 2, "item": "American Hot", "price": 11.99},
            {"item_number": 3, "item": "Margarita", "price": 8.99},
        ]
    
    def view(self):
        return "Welcome to Tom's rad pizzeria!\n\n Menu:\n\n 1) Pepperoni - £9.99\n 2) American Hot - £11.99\n 3) Margarita - £8.99"