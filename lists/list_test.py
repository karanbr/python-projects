
names_list = [
    "Karan",
    "Richard",
    "Hendrik"
]

for name in names_list:
    print(name)

names_list.append("Brüllau")
if names_list.__contains__("Karan"):
    print("YES")


def print_list_items(x: list):
    for i in x:
        print(i)


print_list_items(names_list)
