# file = open("text_file.txt")
# file_content = file.read()
# # print(file)
# print(file_content)
# file.close()
#
# with open("text_file.txt") as text_file:
#     content = text_file.read()
#     print(content)

# mode="r" -> Read only; mode="w" -> Overwrite everything; mode="a" -> Append to existing text
with open("text_file.txt", mode="a") as text_file:
    text_file.write("\nBooya")
