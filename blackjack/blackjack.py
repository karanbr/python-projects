import art
import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, "Jack", "Queen", "King", "Ace"]


def hand_out_card():
    num = random.randint(1, len(cards) - 1)
    value = cards[num]
    cards.remove(cards[num])
    return value


def hit_or_stop():
    answer = input("Hit or stop playing? (hit/stop): ").lower()
    if answer == "hit":
        return True
    else:
        return False


def calculate_card_values(card_list: list):
    value = 0
    for index in range(len(card_list)):
        if card_list[index] == "Jack" or card_list[index] == "Queen" or card_list[index] == "King":
            value += 10
        elif card_list[index] == "Ace":
            if value + 11 > 21:
                value += 1
            else:
                value += 11
        else:
            value += card_list[index]

    return value


def play_blackjack():
    print(art.logo)

    game_over = False
    player_wins = None

    while not game_over:
        player_total = 0
        house_total = 0
        player_cards = []
        house_cards = []

        player_cards.append(hand_out_card())
        player_cards.append(hand_out_card())
        house_cards.append(hand_out_card())
        house_cards.append(hand_out_card())

        print(player_cards)
        print(house_cards)

        player_total += calculate_card_values(player_cards)
        house_total += calculate_card_values(house_cards)

        print(f"player card values: {player_total}")
        print(f"house card values: {house_total}")

        if player_total == 21 and house_total == 21:
            game_over = True
            print("Tie game")

        if house_total == 21:
            game_over = True
            print("House wins")

        if player_total == 21:
            game_over = True
            print("BLACKJACK - Player wins")

        while not game_over:
            if calculate_card_values(player_cards) > calculate_card_values(house_cards):
                house_cards.append(hand_out_card())
            if hit_or_stop():
                player_cards.append(hand_out_card())
                print(player_cards)
                print(f"player card values: {calculate_card_values(player_cards)}")
                print(f"house card values: {calculate_card_values(house_cards)}")
                if calculate_card_values(player_cards) == 21:
                    player_wins = True
                    game_over = True
                    print("Player wins")
                elif calculate_card_values(player_cards) > 21:
                    game_over = True
                    player_wins = False
                    print("House wins")

                if calculate_card_values(player_cards) > calculate_card_values(house_cards):
                    house_cards.append(hand_out_card())
            else:
                game_over = True

        # if 21 >= player_total > house_total:
        #     print("Player wins")
        # elif 21 >= house_total > player_total:
        #     print("House wins")

        print(f"player card values: {calculate_card_values(player_cards)}")
        print(f"house card values: {calculate_card_values(house_cards)}")


play_blackjack()
