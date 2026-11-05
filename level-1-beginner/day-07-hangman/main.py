# 0. Setup
from random import choice
from art import logo, attempts_list

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

game_selected_word: str = choice(fruits)

guessed_word: list = []

for l in game_selected_word:
    guessed_word.append('_')

attempts_number = 6

print(logo)

while attempts_number > 0:
    print("\n" + f"{' '.join(guessed_word)}")
    print(f"You have {attempts_number} attempts.")
    
    user_selected_letter: str = input("Select a letter: ").strip().lower()[0]
    
    if user_selected_letter in selected_letters:
        print("You've already chosen this letter")
    else:
        selected_letters.append(user_selected_letter)
        
        if user_selected_letter in game_selected_word:
            print(f"You guessed the letter {user_selected_letter.upper()}.")
            for k, v in enumerate(game_selected_word):

                if user_selected_letter == v:
                    guessed_word[k] = v
            
            if '_' not in guessed_word:
                print("\n" + f"You discovery the word {game_selected_word.upper()}. Congratulations!")
                break
        else:
            print(f"The letter {user_selected_letter.upper()} isn't in the word.")
            attempts_number -= 1

            print(attempts_list[attempts_number])

            if attempts_number == 0:
                print(f"The word was {game_selected_word.upper()}. You Lose.")