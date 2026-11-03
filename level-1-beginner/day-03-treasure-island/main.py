# Welcome the player
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure" + "\n")

# 1st decision: Crossroad
crossroad_decision: str = input("You're at a cross road. Where do you want to go? Type 'left' or right' ").strip().lower()

if crossroad_decision == 'left':
    print("\n" + "You walked for a few hours and came upon a lake.")
    print("There is an island in the middle of the lake.")

    # 2nd decision: Lake
    lake_decision: str = input("Type 'wait' to wait for a boat, or type 'swim' to swim across. ").strip().lower()

    if lake_decision == 'wait':
        print("\n" + "You made a safe, yet restless, crossing across the lake.")
        print("There is a house with three doors.")

        # 3rd decision: House
        house_decision: str = input("One red, one yellow and one blue. Which colour do you choose? ").strip().lower()

        match house_decision:
            case 'yellow':
                print("You went through the right door and found a safe place to wait for help. Congratulations.")
            case 'red':
                print("The doors closed, and the room quickly caught fire. Game Over.")
            case 'blue':
                print("The doors closed, and the room was flooded. Game Over")
            case _:
                print("Your hesitation in choosing a door caused fatigue to get the better of you. Game Over")

    elif lake_decision == 'swim':
        print("You was devoured by the lake serpent. Game Over.")
    else:
        print("You took too long, some monsters showed up and captured you. Game Over.")

else:
    print("You chose the wrong direction and was caught by a monster. Game Over.")