from random import randint

def select_rock_paper_scissors() -> int:
    """
    Selects an option between 0 and 2 for the Rock, Paper and Scissors game.

    Returns:
        An integer, where 0 is equivalent to rock, 1 to paper and 2 for scissors.
    """
    while True:
        try:
            option_number: int = int(input("Select 0 for Rock, 1 for Paper or 2 for Scissors: ").strip())

            if option_number not in range(0, 3):
                print("Please, choose a option between 0, 1 or 2" + "\n")
            else:
                return option_number
                
        except ValueError:
            print("Please, choose a option between 0, 1 or 2" + "\n")
        except Exception as e:
            print(type(e))
            print(e)

game_options_list: list = ['Rock', 'Paper', 'Scissors']
game_art: list = [
"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
          __________)
      (____)
---.__(___)
"""
]

player_option: int = select_rock_paper_scissors()
com_option: int = randint(0, 2)

print(game_art[player_option])
print("Computer chose: ")
print(game_art[com_option])

if player_option == com_option:
    print("It's a Draw.")
elif player_option == 0:
    if com_option == 1:
        print("You lose.")
    else:
        print("You won!")

elif player_option == 1:
    if com_option == 2:
        print("You lose.")
    else:
        print("You won!")

elif player_option == 2:
    if com_option == 0:
        print("You lose.")
    else:
        print("You won!")