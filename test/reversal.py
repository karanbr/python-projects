def reverse_list(starting_list: list):
    i = len(starting_list) - 1
    reversed_list = []
    while i >= 0:
        index = 0
        reversed_list.append(starting_list[i])
        index += 1
        i -= 1
    return reversed_list


def sort_list(starting_list: list):
    sorted_list = []
    i = 0
    while i < len(starting_list):
        pass


demo_list = [1, 2, 3, 10, 100]
print(reverse_list(demo_list))
print(demo_list[::-1])
