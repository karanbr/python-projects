# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

final_age = 90
age_number = int(age)
years_left = final_age - age_number
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(
    f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")
