import math


def paint_calc(wall_height, wall_width, can_coverage):
    area = (wall_height * wall_width)
    num_of_cans = math.ceil(area / coverage)
    print(f"You'll need {num_of_cans} cans of paint")


# area_calc(wall_height=2, wall_width=4, can_coverage=5)
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(wall_height=test_h, wall_width=test_w, can_coverage=coverage)
