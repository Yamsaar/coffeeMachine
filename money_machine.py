class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
        }

    def __init__(self):
        self.profit = 0
        self.payment = 0

    def report(self):
        """current profits"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def inserting_coins(self):
        """Returns the total calculated from coins inserted."""
        print("please insert the coins.")
        for coins in self.COIN_VALUES:
            self.payment += int(input(f"How many {coins}?: ")) * self.COIN_VALUES[coins]
        return self.payment

    def money_transfer_successfully(self, drink_cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        self.inserting_coins()
        if self.payment >= drink_cost:
            excess_payment = round(self.payment - drink_cost, 2)
            print(f"Here is your change: {excess_payment}{self.CURRENCY}")
            self.profit += drink_cost
            self.payment = 0
            return True
        else:
            print("Sorry that is not enough coins for the beverage. Money refunded")
            self.payment = 0
            return False
