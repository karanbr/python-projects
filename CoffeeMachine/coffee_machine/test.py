import data


def return_coffee(input_string):
    for item in data.MENU:
        if item == input_string:
            print("BOOYA")


return_coffee("latte")

# def enough_resources(resources_input, coffee_input):
#     is_enough = False
#     for resource in resources_input:
#         if resources_input[resource] < coffee_input["ingredients"][resource]:
#             print(f"We're out of {coffee_input}")
#             is_enough = False
#         else:
#             for item in resources_input:
#                 resources_input[item] -= coffee_input["ingredients"][item]
#             print(f"remaining resources: {resources_input}")
#             is_enough = True
#
#     return is_enough

# def enough_resources(resources_input, coffee_input):
#     if ((resources_input["water"] >= coffee_input["ingredients"]["water"])
#             and (resources_input["milk"] >= coffee_input["ingredients"]["milk"])
#             and (resources_input["coffee"] >= coffee_input["ingredients"]["coffee"])):
#
#         for item in resources_input:
#             resources_input[item] -= coffee_input["ingredients"][item]
#         print(f"remaining resources: {resources_input}")
#         return True
#     else:
#         print("Sorry we are out")
#         return False
