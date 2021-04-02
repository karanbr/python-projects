import cipher_tools as alphabet


def encrypt(text_input: str, shift_input: int):
    cipher_text = ""
    for letter in text_input:
        position = alphabet.alphabet.index(letter)
        new_position = position + shift_input
        new_letter = alphabet.alphabet[new_position]
        cipher_text += new_letter

    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text: str, shift_input: int):
    decrypt_text = ""
    for letter in cipher_text:
        position = alphabet.alphabet.index(letter)
        new_position = position - shift_input
        decrypt_text += alphabet.alphabet[new_position]

    print(f"The decoded text is {decrypt_text}")


def run_again():
    answer = input("Use App or quit? (u/q)").lower()
    if answer == "u":
        run()
    else:
        pass


def run():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text_input=text, shift_input=shift)
        run_again()
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(cipher_text=text, shift_input=shift)
        run_again()


run_again()
# def encrypt(text_input: str, shift_input: int):
#     text_list = []
#     for letter in text_input:
#         text_list.append(letter)
#     for index in range(len(text_list)):
#         text_list[index] = alphabet[index + shift_input]
#     print("".join(text_list))
