# Title:  Random Dice
# Author:  Ryan Hawkins
# Updated:  2019-11-08

import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


keep_going = True

player_wins = 0
player_losses = 0
player_ties = 0

clear()
print("---" * 7)
print("Random Dice")
print("---" * 7)

while keep_going:

    play = input("Roll dice? (Y or N)")
    play = play.upper()

    if play == "Y":

        clear()

        player_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)

        print("---" * 7)
        if player_roll > computer_roll:
            print("\tYou win.")
            player_wins += 1
        elif player_roll == computer_roll:
            player_ties += 1
            print("\tIt's a tie.")
        else:
            print("\tYou lose.")
            player_losses += 1

        print()
        print("\tPlayer:", player_roll)
        print("\tComputer:", computer_roll)
        print("---" * 7)

    elif play == "N":
        keep_going = False

    else:
        pass

clear()

print("---" * 7)
print("\tWins:\t", player_wins)
print("\tTies:\t", player_ties)
print("\tLosses:\t", player_losses)
print("---" * 7)
print("Goodbye.")
print((f"Wins:\t{player_wins}").center(21))
print((f"Losses:\t{player_losses}").center(21))