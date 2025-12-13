from menu import MENU, resources

# lets start 
report_dict = resources.copy()
report_dict["money"] = 0.0
def process_report(drink):
    '''for full report with money in machine'''

    report_dict["water"] -= MENU[drink]["ingredients"]["water"]
    if "milk" in MENU[drink]["ingredients"]:
        report_dict["milk"] -= MENU[drink]["ingredients"]["milk"]
    report_dict["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    report_dict["money"] += MENU[drink]["cost"]

def process_coins(drink):
    '''process coins for drink as argument
    and return change(if any)'''
    print("Please insert money: ")
    quarters = float(input("How many quarters: "))
    dimes = float(input("How many dimes: "))
    nickels = float(input("How many nickels: "))
    pennies = float(input("How many pennies: "))
    user_money = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    req_cost = MENU[drink]["cost"]
    change = round(user_money - req_cost, 2)
    if change >= 0:
        process_report(drink)
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink}. Enjoy!")
        user_input()
    else:
        print(f"Sorry that's not enough money. Money Refunded.")
        user_input()

def check_availabilty_resources(drink):
    '''have to check in drink actual req and compare it with report_dict to return 
    the availability'''

    for key, required in MENU[drink]["ingredients"].items():
        if required > report_dict[key]:
            print(f"{key} is not enough. hence, Drink is not Available.")
            return False
    return True
            
def user_input():
    user_drink = input("What would you like?").lower()
    if user_drink == "report":
        # have to show up the current state of resources
        print(f"Water: {report_dict['water']}ml")
        print(f"Milk: {report_dict['milk']}ml")
        print(f"Coffee: {report_dict['coffee']}g")
        print(f"Money: ${report_dict['money']}")
        user_input()
    elif user_drink == "off":
        return
    elif user_drink in MENU:
        if check_availabilty_resources(user_drink):
            process_coins(user_drink)
    else:
        print("Invalid Entry")
        user_input()

user_input()
