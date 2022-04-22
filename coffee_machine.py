class CoffeeMachine:
    def __init__(self):
        """coffeeMachine supply ingredients."""
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def checking_lack_resources(self, order):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in order.ingredients:
            if order.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item} to make the beverage")
                return False

        return True

    def make_report(self):
        print("Status of components in the coffee machine: \n")
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def make_coffee(self, drink):
        """Deduct the required ingredients from the Machine resources."""
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name} ☕. Enjoy")
