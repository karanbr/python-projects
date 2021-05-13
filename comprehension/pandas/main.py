import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_dataframe = pandas.DataFrame(student_dict)
print("**********************")
print("DATAFRAME:")
print(student_dataframe)
print("**********************")

print("**********************")
print("ALL VALUES")
for (key, value) in student_dataframe.items():
    print(value)  # shows all values and not a single one like we want
print("**********************")

print("**********************")
print("INBUILT LOOP")
# instead use inbuilt loop called iterrows -> Loop through rows of df
for (index, row) in student_dataframe.iterrows():
    # print(row)
    print(row.student)
print("**********************")

for (index, row) in student_dataframe.iterrows():
    print(row.score)

print("**********************")
for (index, row) in student_dataframe.iterrows():
    if row.student == "Angela":
        print(row.score)
