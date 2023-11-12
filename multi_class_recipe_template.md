# {{PROBLEM}} Multi-Class Planned Design Recipe

```python
class Menu:
    # User-facing properties:
    #   tracks: list of instances of Track

    def __init__(self):
        # self._menu = [{"item_number":"1","price":"9.99", "item":"Pepperoni Pizza"}]
        # constructs menu as a list of dictionaries 
    
        pass 

    def view(self):
    
        # Side-effects:
        #  formats the menu prop so the customer can read a nicely formatted menu
        #  ... with each menu item numbered
        pass 



class Order:
    def __init__(self, menu):
        # Parameters:
        # menu - an instance of the Menu class
        # Side-effects:
        # Sets menu properties
        # Initializes a list to store chosen menu items
        pass 

    def add_to_basket(self, item_number, quantity ):
        # side effects: appends selected menu items to the list 
        # Returns:
        #   Message confirming the order is placed
        pass # No code here yet

    def view_basket():
        # returns an itemized list, formatted list of menu items and calculates the grand total 

    def confirm(phone_number):
        # initializes an instance of the Confirmation class
        # calls Confirmation#confirm_order

class Confirmation():
        def __init__(self, number):
            # Parameters:
                # number - customer phone number
                # checks for a valid number 
            pass

        def confirm_with_text()
            # sends a text to customer with an estimated time of arrival
            # use time library to get local time, add 40 mins and format to hours and minutes 
            pass
```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python



# Order class

"""
X- An instance of menu is initialized with and the prop can be accessed
"""
menu = Menu()
order = Order(menu)

assert order.menu == == [{"item_number": 1, "item": "Pepperoni Pizza", "price":"9.99"
}, {"item_number": 2, "item": "American Hot", "price":"11.99"
}, {"item_number": 3, "item": "Margarita", "price":"8.99"
}]


"""
X - Order#add_to_basket will return a nice message confirming the order has been placed
"""

menu = Menu()
order = Order(menu)

assert order.add_to_basket(2, 4) == "Your items have been add to your basket"


"""
Order#view_basket will return a formatted receipt of items a with the
total cost calculated
"""
menu = Menu()
order = Order(menu)

assert order.view_basket(2, 2) == "Your order:\n 2) American Hot - £11.99\n 2) American Hot - £11.99\nGrand total: £23.98"


"""
Order#place_order will throw an error if item_number and quantity is
missing
"""
menu = Menu()
order = Order(menu)

with pytest.raises(Exception) as e:
    order.add_to_basket(None, None)
assert str(e.value) == "Error: you must enter an item number and quantity"

"""
Order#add_to_basket will throw an error if item_number is
missing
"""
menu = Menu()
order = Order(menu)

with pytest.raises(Exception) as e:
    order.add_to_basket(1, None)

assert str(e.value) == "Error: you must enter an item number and quantity"


"""
Order#add_to_basket will throw an error if quantity is
missing
"""
menu = Menu()
order = Order(menu)

with pytest.raises(Exception) as e:
    order.add_to_basket(None, 5)

assert str(e.value) == "Error: you must enter an item number and quantity"

"""
Order#add_to_basket will throw an error if quantity is 0
"""
menu = Menu()
order = Order(menu)

with pytest.raises(Exception) as e:
    order.add_to_basket(1, 0)

assert str(e.value) == "Error: You must enter a quantity of 1 or more"


# Confirmation class

"""
Throws error if phone number is not valid mobile number
"""
with pytest.raises(Exception) as excinfo:
        confirmation = Confirmation(438438383485)
    assert str(excinfo.value) == "Error: enter a valid uk mobile number"

"""
Create mock for twilio, need to do more research into
twilio's functionality

should set basket to []
"""

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

# Menu class

"""
X The menu should be initialized as a prop
"""
menu = Menu()

assert menu.menu == [{"item_number": 1, "item": "Pepperoni Pizza", "price":"9.99"
}, {"item_number": 2, "item": "American Hot", "price":"11.99"
}, {"item_number": 3, "item": "Margarita", "price":"8.99"
}]


"""
Given a menu is initialized, Menu#view should return a formatted version
Of the menu which is nice to read
"""
menu = Menu()

assert menu.view() == "Welcome to Tom's rad pizzeria!\n Menu:\n 1) Pepperoni - £9.99\n 2) American Hot - £11.99\n 3) Margarita - £8.99"

# Order class

"""
Order will throw error with no argument
"""
 
    with pytest.raises(Exception) as excinfo:
        order = Order(None)
    assert str(excinfo.value) == "Error: no menu class"



_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->