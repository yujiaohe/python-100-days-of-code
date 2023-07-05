from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

continue_flag = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while continue_flag:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        continue_flag = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(
                drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
