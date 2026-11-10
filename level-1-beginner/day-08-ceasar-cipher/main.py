from art import logo

LETTERS_LIST: list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

def get_mode() -> str:
    """
    Collect the text indicating whether the user will encode or decode a message.

    Returns:
        Returns the processed and cleaned text for use in the 'ceasar_cypher' function.
    """
    while True:
        type: str = input("Type 'encode' to encrypt; type 'decode' to decrypt: ").strip().lower()

        if type in ['encode', 'decode']:
            return type
        else:
            print("Type only 'encode' or 'decode'." + "\n")

def get_shift_number() -> int:
    """
    Get the user's shift number input, preventing the entry of other types of text.

    Returns:
        Returns the shift number, properly converted
    """
    while True:
        try:
            number: int = int(input("Insert the shift number: "))
            return number
        except ValueError:
            print("The shift number needs to be an integer.")
        except Exception as e:
            print(type(e))
            print(e)
            

def ceasar_cipher(type: str, message: str, shift_number: int) -> str:
    """
    Encodes or decodes a message using a shift number provided by the user. 

    Args:
        type: Indicates whether the user wants to encode or decode the message.
        messsage: The message the user wants to encode or decode.
        shift_number: Number of characters the user wants to encode or decode in the message.
    
    Returns:
        The message is encoded if the user selects 'encode', or decoded if the user selects 'decode'.
    """
    formatted_message: str = message.lower().strip()
    shift_number: int = abs(shift_number) % 26

    output_text: str = ''
    
    for letter in formatted_message:

        if letter in LETTERS_LIST:
            position: int = LETTERS_LIST.index(letter)

            if type == 'encode':
                output_text += LETTERS_LIST[position + shift_number]
            if type == 'decode':
                output_text += LETTERS_LIST[position - shift_number]
        else:
            output_text += letter

    return output_text

print(logo)

continue_cypher: bool = True

while continue_cypher:
    cipher_mode: str = get_mode()
    message: str = input("Type your message: ")
    shift_number: int = get_shift_number()

    encoded_message: str = ceasar_cipher(cipher_mode, message, shift_number)
    print(encoded_message)

    finish_cipher: str = input("Type 'yes' if you want to go again. Otherwise type 'no': ").strip().lower()

    if finish_cipher == 'no':
        continue_cypher = False
        print("Cipher closed.")