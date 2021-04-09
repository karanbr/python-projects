import data


def check_valid(menu_input: str):
    if menu_input == "espresso" or menu_input == "latte" or menu_input == "cappuccino":
        return True
    else:
        print("Invalid input. Try again")
        return False


def return_menu_item(string_input):
    for item in data.MENU:
        if item == string_input:
            return data.MENU[item]


def return_price(coffee_type):
    return data.MENU[coffee_type]["cost"]


def take_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickels? "))
    pennies = int(input("How many pennies?"))
    payed_amount = (
            (data.coins["Quarter"] * quarters) + (data.coins["Dime"] * dimes)
            + (data.coins["Nickel"] * nickles) + (data.coins["Penny"] * pennies)
    )
    print(f"quarters x{quarters}\n"
          f"dimes x{dimes}\n"
          f"nickles x{nickles}\n"
          f"pennies x{pennies}\n")
    rounded_amount = round(payed_amount, 3)
    print(f"Total amount payed: {rounded_amount}")
    return rounded_amount


def is_enough_money(menu_price, payed_amount):
    if payed_amount >= menu_price:
        return True
    else:
        print("Not enough money!")
        return False


def change(menu_price, payed_amount):
    return payed_amount - menu_price


def change_coins(change_input):
    coins = {}
    rest = change_input

    if rest / 0.25 >= 0:
        quarters = int(rest / 0.25)
        rest = round(rest % 0.25, 3)
        coins["Quarters"] = quarters
    if rest / 0.10 >= 0:
        dimes = int(rest / 0.10)
        rest = round(rest % 0.10, 3)
        coins["Dimes"] = dimes
    if rest / 0.05 >= 0:
        nickel = int(rest / 0.05)
        rest = round(rest % 0.05, 3)
        coins["Nickels"] = nickel
    if rest / 0.01 >= 0:
        pennies = int(rest / 0.01)
        rest = round(rest % 0.01, 3)
        if rest > 0:
            pennies += 1
        coins["Pennies"] = pennies

    return coins


def enough_resources(resources_input, coffee_input):
    for item in resources_input:
        if resources_input[item] < coffee_input["ingredients"][item]:
            print(f"Sorry! We are out of {item}")
            return False

    for ingredient in resources_input:
        resources_input[ingredient] -= coffee_input["ingredients"][ingredient]
    return True


def print_report(resources_stock: dict):
    print(f"Resources left inside coffee machine")
    for item in resources_stock:
        print(f"{item}: {resources_stock[item]}")


def buy_coffee():
    run_machine = True
    resources_stock = data.resources
    while run_machine:
        coffee_choice = input(f"What would you like? espresso/latte/cappuccino: ").lower()

        if coffee_choice == "off":
            print("Shutting down...")
            run_machine = False

        elif coffee_choice == "report":
            print_report(resources_stock)

        elif check_valid(coffee_choice):
            coffee = return_menu_item(coffee_choice)
            print(coffee)
            if enough_resources(resources_input=resources_stock, coffee_input=coffee):
                price = return_price(coffee_choice)
                print(f"price: {price}")
                payed_amount = take_coins()
                if is_enough_money(menu_price=price, payed_amount=payed_amount):
                    change_back = change(menu_price=price, payed_amount=payed_amount)
                    print(f"Your change total: {change_back}")
                    coins = change_coins(change_input=change_back)
                    for coin in coins:
                        print(f"Your change in {coins[coin]}")
                    print(f"Here is your {coffee_choice}. Enjoy")
            # else:
            #     pass
        else:
            buy_coffee()


if __name__ == '__main__':
    # while True:
    buy_coffee()
