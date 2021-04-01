# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input(f"How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# easy_password_list = []
# for letter in range(0, nr_letters):
#     easy_password_list.append(letters[letter])

# for number in range(0, nr_numbers):
#     easy_password_list.append(numbers[number])

# for symbol in range(0, nr_symbols):
#     easy_password_list.append(symbols[symbol])

# password_str = "".join(easy_password_list)
# print(f"Easy password: {password_str}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password_list = []
for letter in range(0, nr_letters):
    random_index = random.randint(0, (len(letters) - 1))
    hard_password_list.append(letters[random_index])

for number in range(0, nr_numbers):
    random_index = random.randint(0, (len(numbers) - 1))
    hard_password_list.append(numbers[random_index])

for symbol in range(0, nr_symbols):
    random_index = random.randint(0, (len(symbols) - 1))
    hard_password_list.append(symbols[random_index])

print(hard_password_list)

shuffled_list = []

for i in range(0, len(hard_password_list)):
    random_index = random.randint(0, (len(hard_password_list) - 1))
    shuffled_list.append(hard_password_list[random_index])
    hard_password_list.remove(hard_password_list[random_index])

# print(hard_password_list)
# print(shuffled_list)

# master_password = "".join(shuffled_list)
master_password = ""
for char in shuffled_list:
    master_password = master_password + char

print(f"hard password: {master_password}")
