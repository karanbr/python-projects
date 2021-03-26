# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_in_meters = float(height)
weight_in_kg = float(weight)
height_squared_in_meters = height_in_meters ** 2

bmi = weight_in_kg / height_squared_in_meters
bmi_rounded = round(bmi)

interpretation = ""

if bmi_rounded < 18.5:
    interpretation = " underweight"
elif bmi_rounded >= 18.5 and bmi_rounded < 25:
    interpretation = " normal weight"
elif bmi_rounded >= 25 and bmi_rounded < 30:
    interpretation = " slightly overweight"
elif bmi_rounded >= 30 and bmi_rounded < 35:
    interpretation = " obese"
else:
    interpretation = " clinically obese"

print(f"Your BMI is {bmi_rounded}, you are {interpretation}")
