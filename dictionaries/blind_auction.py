import bid_art


def add_bidder_to_dict(name: str, bid: float, bidders: dict):
    bidders[name] = bid


def run_bidding_app():

    print(bid_art.logo)

    bidders = {}

    name = input("Enter your name: ")
    bid = float(input("Enter your bid: $"))
    add_bidder_to_dict(name=name, bid=bid, bidders=bidders)

    answer = input("Are there other people who want to bid? (y/n) ").lower()
    while answer == "y":
        name = input("Enter your name: ")
        bid = float(input("Enter your bid: "))
        add_bidder_to_dict(name=name, bid=bid, bidders=bidders)
        answer = input("Are there other people who want to bid? (y/n) ").lower()

    max_bid = 0
    highest_bidder = "No one"
    for bidder in bidders:
        bidders_value = bidders[bidder]
        if bidders_value > max_bid:
            max_bid = bidders_value
            highest_bidder = bidder

    print(f"The highest bid is {max_bid} by {highest_bidder}")


run_bidding_app()
