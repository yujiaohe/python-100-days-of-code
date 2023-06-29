MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    """Print current resource values"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_sufficient(coffee_type):
    """Return True/False to indicator resource sufficiency and print message if not sufficient"""
    sufficient = True
    for item in coffee_type["ingredients"]:
        if resources[item] < coffee_type["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            sufficient = False
    return sufficient


def process_coin():
    """Return total coins received from user"""
    print("Please insert coins.")
    total_coins = 0
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }
    # process coins
    for key in coins:
        coins[key] *= int(input(f"how many {key}?: "))
        total_coins += coins[key]
    return total_coins


def check_transaction(coffee_cost, payed):
    """Return True/False to check user has inserted enough money for selected drink"""
    if payed < coffee_cost:
        return False
    else:
        return True


def make_coffee(coffee_type):
    """Update resources according to drink type"""
    for item in coffee_type["ingredients"]:
        resources[item] -= coffee_type["ingredients"][item]


money = 0
continue_flag = True
while continue_flag:
    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'report':
        report()
    elif choice == 'off':
        continue_flag = False
    else:
        drink = MENU[choice]
        if check_sufficient(drink):
            coffee_cost = drink["cost"]
            total_coins = process_coin()
            if check_transaction(coffee_cost, total_coins):
                make_coffee(drink)
                money += coffee_cost
                return_coins = round(total_coins - coffee_cost, 2)
                print(f"Here is ${return_coins} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
