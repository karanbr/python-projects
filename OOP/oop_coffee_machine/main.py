from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def run_machine():
    machine_running = True
    while machine_running:
        print(menu.get_items())
        choice_string = input("What would you like?: ").lower()
        if choice_string == "report":
            coffee_maker.report()
            money_machine.report()
        elif choice_string == "off":
            machine_running = False
        else:
            coffee = menu.find_drink(choice_string)
            print(f"You have chosen: {coffee.name}. Price: ${coffee.cost}")
            if coffee_maker.is_resource_sufficient(coffee):
                if money_machine.make_payment(coffee.cost):
                    coffee_maker.make_coffee(coffee)


if __name__ == '__main__':
    run_machine()
