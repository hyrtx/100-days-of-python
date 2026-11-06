LETTERS_LIST: list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

def ceasar_cipher(type: str, message: str, shift_number: 9) -> str:
    """
    test

    Args:
        type: text
        messsage: text
        shift_number: text
    
    Returns:
        text
    """
    formatted_message: str = message.lower().strip()

    if shift_number > 26:
        shift_number = shift_number % 26

    if type == 'encode':
        encrypted_message: list = []
        
        for letter in formatted_message:

            if letter in LETTERS_LIST:
                position: int = LETTERS_LIST.index(letter)
                encrypted_message.append(LETTERS_LIST[position + shift_number])
            else:
                encrypted_message.append(letter)

        return ''.join(encrypted_message)
    
    if type == 'decode':
        decoded_message: list = []

test = ceasar_cipher('encode', 'Hello World!', 9)
print(test)