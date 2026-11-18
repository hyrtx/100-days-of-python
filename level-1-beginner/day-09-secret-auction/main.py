import os
from art import logo

def clear_console() -> None:
    """
    Clear the terminal depending on the operating system.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def submit_bid() -> dict:
    """
    Collects a bid from an auction participant.

    Returns:
        A dictionary with the name and bid value from a participant.
    """
    name: str = input("What is your name? ").strip().capitalize()

    while True:
        try:
            bid_value: float = float(input("What's your bid? ").strip())
            break
        except ValueError:
            print("Please, submit only numeric characters in the bid.")
        except Exception as e:
            print(type(e))
            print(e)
    
    bid_registration: dict = {
        name: bid_value
    }

    return bid_registration

def auction() -> list:
    """
    Records all bids from the auction in a dictionary.

    Returns:
        A dictionary mapping bidder names to their bid values.
    """

    auction_bids: dict = {}

    while True:
        bid_record: dict = submit_bid()
        auction_bids.update(bid_record)

        close_bidding: str = input("Are there any other bidders? Type 'yes' or 'no'. ").strip().lower()[0]
        clear_console()

        if close_bidding == 'n':
            return auction_bids

print(logo)
print("Welcome to the secret auction program.")

auction_record: dict = auction()

auction_winner: str
winner_bid: float
auction_winner, winner_bid = max(auction_record.items(), key=lambda x: x[1])

print(f"The winner is {auction_winner} with a bid of ${winner_bid:.2f}.")