import calculator_art

operations = ["+", "-", "*", "/"]


def print_operations():
    for operator in operations:
        print(operator)


def pick_operation(operation_input):
    if operation_input == "+":
        return operations[0]
    elif operation_input == "-":
        return operations[1]
    elif operation_input == "*":
        return operations[2]
    elif operation_input == "/":
        return operations[3]
    else:
        print("Invalid input")
        return


def calculate(n1: float, n2: float, operation: str):
    if operation == "+":
        return n1 + n2
    elif operation == "-":
        return n1 - n2
    elif operation == "*":
        return n1 * n2
    elif operation == "/":
        return n1 / n2
    else:
        return


def run_again():
    answer = input("Use calculator? (y/n)").lower()
    if answer == "y":
        run_calculator()
    else:
        pass


def run_calculator():
    print(calculator_art.logo)
    first_number = float(input("What's the first number?: "))
    print_operations()
    should_continue = True

    while should_continue:
        operation = input("Pick an operation: ")
        second_number = float(input("Whats the next number?: "))
        result = calculate(n1=first_number, n2=second_number, operation=operation)
        print(result)
        # continue_calc(result)
        if input(f"Continue calculating with {result}? (y/n)") == "y":
            first_number = result
        else:
            should_continue = False
            run_again()


run_again()

# def continue_calc(prev_result: float):
#     end_of_calc = False
#     answer = input(f"Type 'y' to continue calculating with {prev_result} or type 'n' to exit").lower()
#     while not end_of_calc:
#         new_operation = input("Pick an operation: ")
#         next_number = float(input("Whats the next number?: "))
#         return calculate(n1=prev_result, n2=next_number, operation=new_operation)
#         answer = input(f"Type 'y' to continue calculating with {prev_result} or type 'n' to exit").lower()
