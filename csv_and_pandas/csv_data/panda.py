import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

print(type(data))           # Type: Dataframe --> Like a whole table
print(type(data["temp"]))   # Type: Series --> Like a single column as a list

data_dict = data.to_dict()  # Convert a Dataframe into a python dictionary
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# Calculate average temperatures (Normal way):
total = sum(temp_list)
average_temp = total / len(temp_list)
print(f"Average temp is: {round(average_temp, 2)}°")

# Calculate average temperatures (With Pandas):
average_temp_pandas = data["temp"].mean()
print(average_temp_pandas.round(2))

# Find maximum temperature with pandas series method
max_temp = data["temp"].max()
print(f"Max temperature: {max_temp}°")

# Instead of accessing a column with data["temp"] you can also access it with:
print(data.temp)
print(data.condition)

# Get a row of data:
row = data[data.day == "Monday"]
print(f"Row Monday:\n {row}")

# Get row with highest temperature:
print("Row with highest temperature:")
max_temp_row = data[data.temp == data.temp.max()]
print(max_temp_row)

# Get specific data from specific row
print("Get condition for Monday")
monday = data[data.day == "Monday"]
print(monday.condition)

# Get temp for monday
print("Get Temperature for Monday")
monday_temp = data[data.day == "Monday"]
print(f"Monday temperature in Celsius: {int(monday_temp.temp)}")
monday_temp_farenheit = int(monday_temp.temp) * 9/5 + 32
print(f"Monday temperature in Farenheit: {monday_temp_farenheit}")

# Create Dataframe from scratch
student_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

dataframe = pandas.DataFrame(student_dict)
print(dataframe)
dataframe.to_csv("student_data.csv")
