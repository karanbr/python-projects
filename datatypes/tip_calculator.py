print("Welcome to the top calculator")

bill_amount = input("What was the total bill?\n")
num_of_people = input("How many people to split the bill?\n")
tip_percentage = input("What percentage tip would you like to give?\n")

bill_amount_float = float(bill_amount)
num_of_people_int = int(num_of_people)
tip_percentage_decimal = float(tip_percentage) / 100

total_bill_with_tip = bill_amount_float + \
    (bill_amount_float * tip_percentage_decimal)
individual_amount = total_bill_with_tip / num_of_people_int

individual_amount_rounded = round(individual_amount, 2)

print(f"Each person should pay ${individual_amount_rounded}")
