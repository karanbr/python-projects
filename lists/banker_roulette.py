import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

num_of_people = len(names)
chosen_one = random.randint(0, num_of_people - 1)
bill_payer = names[chosen_one]

print(f"{bill_payer} is going to pay the bill today")
