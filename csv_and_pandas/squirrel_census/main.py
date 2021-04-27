import pandas

squirrel_data = pandas.read_csv("squirrel_census2018.csv")
squirrel_data_dict = squirrel_data.to_dict()
# print(squirrel_data_dict)

squirrel_fur_series = squirrel_data["Primary Fur Color"]
# print(squirrel_fur_series)
# black_squirrels = 0
# gray_squirrels = 0
# cinnamon_squirrels = 0

# Also valid
# for color in squirrel_fur_series:
#     if color == "Black":
#         black_squirrels += 1
#     elif color == "Gray":
#         gray_squirrels += 1
#     elif color == "Cinnamon":
#         cinnamon_squirrels += 1

gray_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
print(gray_squirrels)  # All rows with grey squirrels
gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
print(gray_squirrels_count)
print(black_squirrels_count)
print(cinnamon_squirrels_count)

# print(f"Black squirrels: {black_squirrels}")
# print(f"Gray squirrels: {gray_squirrels}")
# print(f"Cinnamon squirrels: {cinnamon_squirrels}")
#
squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
#
squirrel_new_dataframe = pandas.DataFrame(squirrel_dict)
squirrel_new_dataframe.to_csv("squirrel_count.csv")
