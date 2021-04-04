# ################### Scope ####################
#
# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")


enemies = 1


# NOT GOOD
# def increase_enemies():
#     global enemies
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


print(f"enemies outside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
