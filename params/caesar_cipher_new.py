import cipher_tools as cipher


def caesar(text_input: str, shift_input: int, encode_or_decode: str):
    transformed_text = ""

    for char in text_input:
        if char in cipher.alphabet:
            new_position = 0
            position = cipher.alphabet.index(char)
            if encode_or_decode == "encode":
                new_position = position + shift_input
            elif encode_or_decode == "decode":
                new_position = position - shift_input
            else:
                print(f"{encode_or_decode} is not an option. Try again")
                run_again()
            new_letter = cipher.alphabet[new_position]
            transformed_text += new_letter
        else:
            transformed_text += char

    print(f"The {encode_or_decode}d text is {transformed_text}")
    run_again()


def run():
    print(cipher.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    caesar(text_input=text, shift_input=shift, encode_or_decode=direction)


def run_again():
    answer = input("Use App or quit? (u/q): ").lower()
    if answer == "u":
        run()
    else:
        print("Goodbye")
        pass


run_again()
