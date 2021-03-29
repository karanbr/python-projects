# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

true_score = 0
love_score = 0

names = name1.lower() + name2.lower()

# -- true_score --
true_score += names.count("t")
true_score += names.count("r")
true_score += names.count("u")
true_score += names.count("e")

# -- love_score --
love_score += names.count("l")
love_score += names.count("o")
love_score += names.count("v")
love_score += names.count("e")

string_number = str(true_score) + str(love_score)
percentage_number = int(string_number)
# print(f"Number: {percentage_number}")

if percentage_number < 10 or percentage_number > 90:
    print(
        f"Your score is {percentage_number}, you go together like coke and mentos")
elif percentage_number >= 40 and percentage_number <= 50:
    print(f"Your score is {percentage_number}, you are alright together")
else:
    print(f"Your score is {percentage_number}")
