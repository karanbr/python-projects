import random
import art


def easy_or_hard():
    answer = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if answer == "easy":
        return 10
    elif answer == "hard":
        return 5
    else:
        print("Not a valid input! Try again")
        easy_or_hard()


def check_answer(guess, number, guesses_input):
    if guess > number:
        print("Too high")
        return guesses_input - 1
    elif guess < number:
        print("Too low")
        return guesses_input - 1
    else:
        print(f"Correct. The number was {number}")


def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    random_number = random.randint(1, 100)
    guesses = easy_or_hard()
    print(f" Number is: {random_number}")

    answer = ""
    while answer != random_number:
        print(f"You have {guesses} attempts remaining to guess the number.")
        answer = int(input("Make a guess: "))
        guesses = check_answer(answer, random_number, guesses)

        if guesses == 0:
            print("You ran out of guesses. You lose!")
            return
        elif answer != random_number:
            print("Guess again!")

        play_again()


def play_again():
    answer = input("Do you want to play the number guessing game? (y/n): ")
    if answer == "y":
        play_game()
    else:
        pass


play_again()

# while answer != random_number and guesses > 0:
#     if answer > random_number:
#         print("Too high")
#     else:
#         print("Too low")
#     guesses -= 1
#
#     print(f"You have {guesses} attempts remaining to guess the number.")
#     answer = int(input("Make a guess: "))
#
#     if guesses == 0:
#         print("You lose")
#         play_again()
#
# if answer == random_number:
#     print(f"You win! The answer was {random_number}")
#     play_again()
#
# if guesses == 0:
#     print("You lose")
#     play_again()
