import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def print_hand(hand):
    if hand == 0:
        print(rock)
    elif hand == 1:
        print(paper)
    elif hand == 2:
        print(scissors)


def play_game():

    players_choice = input(
        "What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors:\n")
    player_choice_int = int(players_choice)
    print("You chose: ")
    print_hand(player_choice_int)

    computers_choice = random.randint(0, 2)
    print("The Computer chose:")
    print_hand(computers_choice)

    if player_choice_int == 0:
        if computers_choice == 0:
            print("its a tie!")
        elif computers_choice == 1:
            print("Computer wins")
        else:
            print("You win")
        play_again
    elif player_choice_int == 1:
        if computers_choice == 0:
            print("You win")
        elif computers_choice == 1:
            print("its a tie")
        else:
            print("Computer wins")
        play_again()
    elif player_choice_int == 2:
        if computers_choice == 0:
            print("Computer wins")
        elif computers_choice == 1:
            print("You win")
        else:
            print("its a tie")
        play_again()
    else:
        answer = input("Invalid input")
        play_again()


def play_again():
    answer = input("Play again? (y/n)")
    if answer == "y":
        play_game()
    else:
        pass


play_game()
