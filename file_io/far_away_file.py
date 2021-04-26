# Relative Path
with open("../../../hello.txt") as hello:
    content = hello.read()
    print(content)

# Absolute Path
with open("/Users/karan/Desktop/hello.txt") as hello:
    content = hello.read()
    print(content)
