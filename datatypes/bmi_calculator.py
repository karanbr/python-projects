# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_in_meters = float(height)
weight_in_kg = float(weight)
height_squared_in_meters = height_in_meters ** 2

bmi = weight_in_kg / height_squared_in_meters
bmi_rounded = round(bmi)
print("Your BMI is " + str(bmi_rounded))
