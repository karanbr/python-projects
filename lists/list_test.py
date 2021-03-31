
names_list = [
    "Karan",
    "Richard",
    "Hendrik"
]

print(names_list[1])

for name in names_list:
    print(name)

names_list.append("Brüllau")
if names_list.__contains__("Karan"):
    print("YES")


def print_list_items(x: list):
    for i in x:
        print(i)


print_list_items(names_list)

numbers_list = []
numbers_list.append(1)
numbers_list.append(3)
numbers_list.append(2)
print(numbers_list)
numbers_list.sort()
print(numbers_list)
