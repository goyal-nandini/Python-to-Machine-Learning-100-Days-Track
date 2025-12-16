# uses the concept of OOP
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if drink is not None: # 📝✔️🟢
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

# a bug when i type any invalid entry👇 -> correction point added 📝✔️🟢
# 🔥 Root cause (very important)
# find_drink() prints an error, but still returns None, and the main code doesn’t stop execution.

# So:

# Error message is printed ✔️
# Program continues ❌
# None is treated like a MenuItem
# Program crashes 💥
