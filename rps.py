import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPPER = 2
    SCISSORS = 3


play_again = True

while play_again:
    playerchoice = input(
        "\nEnter...\n1 for Rock\n2 for Paper\n3 for Scissor:\n")
    player = int(playerchoice)

    machinechoice = random.choice("123")
    computer = int(machinechoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1 or 2 or 3")
    print("\nYou chose: " + str(RPS(player)).replace("RPS.", ""))
    print("Computer chose: " + str(RPS(computer)).replace("RPS.", ""))
    if (player == 1 and computer == 3) | (player == 2 and computer == 1) | (player == 3 and computer == 2):

        print("🎉🎉🎉 You win! 🎉🎉🎉\n")
    elif player == computer:
        print("😲😲😲😲😲 Tie Game!😲😲😲😲😲\n")
    else:
        print("🎉🎉🎉  🐍 Python wins! 🎉🎉🎉\n")
    play_again = input("Play again?: Y for yes | N for no: ")
    if play_again == "y" or play_again == "Y":
        continue
    else:
        break
sys.exit("Bye Bye!")
