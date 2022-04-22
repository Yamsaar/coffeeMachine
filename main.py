from coffee_machine import CoffeeMachine
from menu import Menu
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMachine()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_item()
    choice = input("\nWhat would you like? (espresso/latte/cappuccino/makiato/double espresso): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.make_report()
        money_machine.report()
    else:
        drink = menu.searching_drink(choice)
        if coffee_maker.checking_lack_resources(drink) and money_machine.money_transfer_successfully(drink.cost):
            coffee_maker.make_coffee(drink)
