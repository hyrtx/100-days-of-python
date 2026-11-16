print("Welcome to the secret auction program.")

def submit_bid() -> dict:
    """
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
        "name": name,
        "bid_value": bid_value
    }

    return bid_registration

auction_record: list = []

while True:
    bid_record: dict = submit_bid()
    auction_record.append(bid_record)

    close_bidding: str = input("Are there any other bidders? Type 'yes' or 'no'. ").strip().lower()[0]

    if close_bidding == 'n':
        break

print(auction_record)