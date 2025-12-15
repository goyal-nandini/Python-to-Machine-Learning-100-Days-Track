from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# lets do this problem then we have to cover day17 also today only...as 19th day
# hey make the object name good not this bad obj1 obj2 eww...
# bugs hai so logical okay hai but program flow error hai -_- but mam wala ek dum same hai so its for yr understanding the correct flow!!
# leaving as it is seems okay for now rest i am checking q&a
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    
    print("What would you like? ")
    drink_options = menu.get_items()
    choice = input(f"Enter your choice from {drink_options}: ").lower()

    drink = menu.find_drink(choice) # vaise too ye find_drink() method hai object return krta hai lets see what happens!!
    if drink: # "off" is being treated like a drink name before you check for "off". A BUG that's why it prints "Sorry that item is not available." when off
        # checking availability
        if coffee_maker.is_resource_sufficient(drink):
            # process coins
            if money_machine.make_payment(drink.cost):
                # make coffee
                coffee_maker.make_coffee(drink)
    # 🚨Command keywords (off, report) must be handled BEFORE business logic (find_drink).
    elif choice == "report": # A BUG that's why it prints "Sorry that item is not available." when report
       coffee_maker.report()
       money_machine.report()
    elif choice == "off": # A BUG that's why it prints "Sorry that item is not available." when off
        is_on = False
    else: # no need i guess it already prints the item is not available (but anyways make it stay!!)
        print("Invalid Choice")