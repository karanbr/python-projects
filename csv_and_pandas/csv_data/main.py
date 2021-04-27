# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#
# print(data)

import csv

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temp = int(row[1])
            temperatures.append(temp)
        # print(row)
    # temps = temperatures[1::]
    print(temperatures)
