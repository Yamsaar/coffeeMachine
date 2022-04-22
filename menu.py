class MenuItems:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItems(name='latte', water=200, milk=150,
                      coffee=24, cost=2.5),
            MenuItems(name='espresso', water=50, milk=0,
                      coffee=18, cost=1.5),
            MenuItems(name='double espresso', water=50, milk=0,
                      coffee=36, cost=1.75),
            MenuItems(name='makiato', water=50, milk=10,
                      coffee=18, cost=2.0),
            MenuItems(name='cappuccino', water=250, milk=100,
                      coffee=24, cost=3.0)
        ]

    def get_item(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}"
        return options

    def searching_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
            else:
                print("sorry this drink is not available.")
