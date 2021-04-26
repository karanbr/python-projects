# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def return_starting_text():
    with open("Input/Letters/starting_letter.txt") as starting_letter:
        starting_content = starting_letter.read()
    return starting_content


with open("Input/Names/invited_names.txt") as names_from_file:
    names = names_from_file.readlines()
    for name in names:
        with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as finished_email:
            content = return_starting_text()
            new_content = content.replace("[name]", name.strip())
            finished_email.write(new_content)
