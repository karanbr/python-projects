import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def hand_out_card():
    """Returns a random card from the deck"""
    return random.choice(cards)


def calculate_card_values(card_list: list):
    """Calculates total value of cards"""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def compare_scores(player_score, house_score):
    if player_score == house_score:
        return "Tie game 🙃"
    elif house_score == 0:
        return "House has a Black Jack 😩"
    elif player_score == 0:
        return "BLACKJACK! You win 😎"
    elif player_score > 21:
        return "You went over. You lose 😕"
    elif house_score > 21:
        return "House went over. You win 😛"
    elif player_score > house_score:
        return "You win 😁"
    else:
        return "You lose 🥲"


def play_blackjack():
    print(art.logo)

    game_over = False
    player_cards = []
    house_cards = []
    player_score = 0
    house_score = 0

    for i in range(2):
        player_cards.append(hand_out_card())
        house_cards.append(hand_out_card())

    while not game_over:

        player_score = calculate_card_values(player_cards)
        house_score = calculate_card_values(house_cards)
        print(f"Players Cards: {player_cards} value: {calculate_card_values(player_cards)}")
        print(f"Houses first Card: {house_cards[0]}")

        if player_score == 0 or house_score == 0 or player_score > 21:
            game_over = True
        else:
            answer = input("Hit or stop playing? (hit/stop)").lower()
            if answer == "hit":
                player_cards.append(hand_out_card())
                player_score = calculate_card_values(player_cards)
            else:
                game_over = True

    while house_score != 0 and house_score < 17:
        house_cards.append(hand_out_card())
        house_score = calculate_card_values(house_cards)

    print(compare_scores(house_score=house_score, player_score=player_score))
    print(f"Your cards were: {player_cards} with value: {player_score}")
    print(f"House cards were: {house_cards} with value: {house_score}")
    play_again()


def play_again():
    print()
    print("*******************************")
    answer = input("Play Blackjack? (y/n): ").lower()
    if answer == "y":
        play_blackjack()
    else:
        pass


play_again()
