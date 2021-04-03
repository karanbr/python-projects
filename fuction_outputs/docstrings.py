
def format_name(first_name: str, surname: str):
    """Take a first and last name and format it
    to return the title case version of the name."""
    if first_name == "" or surname == "":
        return "No valid inputs"
    fullname = first_name.title() + " " + surname.title()
    return fullname

# Docstring -> Explains function when you call it
# Use """xxx"""
