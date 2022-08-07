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


def check_resources(order_ingredient):
    """return true if orders can be made and false if not"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coin():
    """return total calc from coins inserted"""
    total = int(input("How many Quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many Nickel? ")) * 0.05
    total += int(input("How many Quarters? ")) * 0.01
    return total


def check_transc(money_recieved, drink_cost):
    """:return true when the payment is accepted, or false if money is insufficient"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        if change > 0:
            print(f"Kindly take your €{change} change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


profit = 0
machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            print("Please make payment in coins")
            payment = process_coin()
            if check_transc(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])