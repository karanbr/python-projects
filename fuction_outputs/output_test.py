# Functions with Outputs

def format_name(first_name: str, surname: str):
    if first_name == "" or surname == "":
        return "No valid inputs"
    fullname = first_name.title() + " " + surname.title()
    return fullname


name = format_name("kARAN", "bruellau")
print(name)
print(format_name("", ""))
