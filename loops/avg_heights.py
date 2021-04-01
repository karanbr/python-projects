# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
print(student_heights)

height_sum = 0
num_of_heights = 0

for height in student_heights:
    height_sum += height
    num_of_heights += 1

avg_height = height_sum / num_of_heights

print(f"Average hight is {round(avg_height)} cm")
