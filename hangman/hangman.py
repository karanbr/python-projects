import random
import hangman_art
import hangman_words


def play_again():
    answer = input("Play again? (y/n)")
    if answer == "y" or answer == "Y":
        play_game()
    else:
        pass


def play_game():
    word_list = hangman_words.word_list
    chosen_word = random.choice(word_list)
    chosen_word_list = []

    for letters in chosen_word:
        chosen_word_list.append(letters)
    blank = "_"
    lives = 6
    end_of_game = False

    print(hangman_art.logo)

    print(f'Pssst, the solution is {chosen_word}.')

    display = []
    for letter in chosen_word:
        display.append(blank)

    while not end_of_game:
        guess = input("Guess a letter:\n").lower()

        if guess in display:
            print(f"You've already guessed {guess}")

        for index in range(len(chosen_word)):
            letter = chosen_word[index]
            if letter == guess:
                display[index] = letter

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life")
            lives -= 1
            print(f"You have {lives} lives left")
            if lives == 0:
                end_of_game = True
                print("You lose")
                play_again()

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win")
            play_again()

        print(hangman_art.stages[lives])


play_game()
# for index in range(0, len(chosen_word)):
#     if chosen_word_list[index] == guess:
#         display.remove("_")
#         display.insert(index, guess)
