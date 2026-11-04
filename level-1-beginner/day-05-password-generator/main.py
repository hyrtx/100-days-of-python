from random import choices, shuffle

LETTERS_LIST: list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

NUMBERS_LIST: list = [
    '0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9'
]

SPECIAL_CHARS_LIST: list = [
    '!', '@', '#', '$', '%', '&', '*',
    '(', ')', '-', '_', '+', '=', 
    '[', ']', '{', '}', '<', '>',
    '?', '/', '\\', '|', '~', '^',
    ':', ';', '.', ','
]

def generate_password(letters: int, numbers: int, symbols: int) -> str:
    """
    Create a password with letters, numbers and symbols based on the number of characters requested by the user.

    Args:
        letters: Number of requested letters characters.
        numbers: Number of requested numbers characters.
        symbols: Number of requested symbols characters.
    
    Returns:
        A random password with the numbers of characters requested.
    """
    
    print()

    if letters + numbers + symbols == 0:
        print("You entered zeros for each character type when prompted, so we used 4 characters for each.")
        letters: int = 4
        numbers: int = 4
        symbols: int = 4
    
    password_list: list = (
        choices(LETTERS_LIST, k=letters) +
        choices(NUMBERS_LIST, k=numbers) +
        choices(SPECIAL_CHARS_LIST, k=symbols)
    )
    
    shuffle(password_list)
    return ''.join(password_list)

print("Welcome to the password generator")

num_letters: int = int(input("How many letters would you like in your password? ").strip())
num_numbers: int = int(input("How many numbers would you like? ").strip())
num_special_chars: int = int(input("How many symbols would you like? ").strip())

password = generate_password(num_letters, num_numbers, num_special_chars)

print(f"Your password is '{password}'.")