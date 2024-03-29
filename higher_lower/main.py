import art
import game_data as game
import random


def pick(a_or_b):
    num = random.randint(0, len(game.data) - 1)
    print(f"{a_or_b} {game.data[num]['name']}, a {game.data[num]['description']}, from {game.data[num]['country']}")
    return game.data[num]


def check_pick(picked_input: dict, compare_input: dict):
    if picked_input['follower_count'] > compare_input['follower_count']:
        return True
    else:
        return False


def return_picked_dict(pick_a_input: dict, pick_b_input: dict):
    chosen_pick = {}
    other_pick = {}
    print("*****************************************")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    print()
    if answer == "a":
        chosen_pick = pick_a_input
        other_pick = pick_b_input
    elif answer == "b":
        chosen_pick = pick_b_input
        other_pick = pick_a_input
    else:
        print(game.invalid)
        return_picked_dict(pick_a_input, pick_b_input)

    return chosen_pick, other_pick


def play_game():
    score = 0
    game_over = False

    while not game_over:
        print(art.logo)
        pick_a = pick("A:")
        print(art.vs)
        pick_b = pick("B:")
        while pick_a['name'] == pick_b['name']:
            pick_b = pick("B:")
        chosen_pick, other_pick = return_picked_dict(pick_a_input=pick_a, pick_b_input=pick_b)
        print(f"chosen_pick: {chosen_pick}")
        print(f"other pick: {other_pick}")

        if check_pick(picked_input=chosen_pick, compare_input=other_pick):
            for _ in range(10):
                print()
            score += 1
            print(art.stars)
            print(f"{game.correct} {score}")
        else:
            game_over = True
            print(art.stars)
            print(f"{game.game_over} {score}")
            play()


def play():
    answer = input(game.play).lower()
    if answer == "y":
        play_game()
    elif answer == "n":
        pass
    else:
        print(game.invalid)
        play()


play()
