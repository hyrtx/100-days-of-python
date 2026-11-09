LETTERS_LIST: list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

def get_type() -> str:
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

    encrypted_message: list = []
    
    for letter in formatted_message:

        if letter in LETTERS_LIST:
            position: int = LETTERS_LIST.index(letter)

            if type == 'encode':
                encrypted_message.append(LETTERS_LIST[position + shift_number])
            if type == 'decode':
                encrypted_message.append(LETTERS_LIST[(position - shift_number)])
        else:
            encrypted_message.append(letter)

    return ''.join(encrypted_message)

encoded_message: str = ceasar_cipher('encode', 'hello world!', 94)
print(encoded_message)

decoded_message: str = ceasar_cipher('decode', 'xubbe mehbt!', 94)
print(decoded_message)