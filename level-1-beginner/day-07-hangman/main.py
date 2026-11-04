# 0. Setup
from random import choice

fruits: list = [
    "apple",
    "banana",
    "orange",
    "strawberry",
    "grape",
    "watermelon",
    "pineapple",
    "mango",
    "pear",
    "peach",
    "cherry",
    "kiwi",
    "lemon",
    "papaya",
    "coconut"
]

selected_letters: list = []

# 1. A word (fruit) is selected for the user to guess
game_selected_word: str = choice(fruits)

# 2. Generates blank spaces (_) for each letter of the chosen word
guessed_word: list = []

for l in game_selected_word:
    guessed_word.append('_')

# 3. Game Start: User picks a letter
attempts_number = 6

while attempts_number > 0:
    print(game_selected_word) # Remover
    print(f"{' '.join(guessed_word)}")
    print(f"You have {attempts_number} attempts.")

    user_selected_letter: str = input("Select a letter: ").strip().lower()[0]

    if user_selected_letter in selected_letters:
        print("You've already chosen this letter")
    else:
        selected_letters.append(user_selected_letter)

        if user_selected_letter in game_selected_word:
            for k, v in enumerate(game_selected_word):

                if user_selected_letter == v:
                    guessed_word[k] = v
            
            if '_' not in guessed_word:
                print(f"You discovery the word {game_selected_word.upper()}. Congratulations!")
                break
        else:
            attempts_number -= 1