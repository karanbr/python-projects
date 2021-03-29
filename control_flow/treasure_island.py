def play_game():
    display_treasure()
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    choice = input(
        "Your at a crossroads. Do you go left or right? (left/right)\n")

    if choice == "right":
        game_over("You fall into a hole")
    else:
        choice2 = input(
            "You're infront of a lake. Do you swim through or wait? (swim/wait)\n")

        if choice2 == "swim":
            game_over("You drown")
        else:
            choice3 = input(
                "You arrive infront of a 3 doors. One red, blue and yellow. \nWhich door do you take? (blue/red/yellow)\n")

            if choice3 == "yellow":
                print("You win!")
                play_again()
            else:
                game_over("You die by Monkey")


def game_over(message):
    print(f"{message}. You die! Game over!")
    play_again()


def play_again():
    play_again = input("Play again? (y/n)\n")
    if play_again == "y":
        play_game()
    else:
        pass


def display_treasure():
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


play_game()
