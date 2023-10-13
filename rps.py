import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPPER = 2
    SCISSORS = 3


playerchoice = input("Enter...\n1 for Rock\n2 for Paper\n3 for Scissor:\n")
player = int(playerchoice)

machinechoice = random.choice("123")
computer = int(machinechoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1 or 2 or 3")
print("\nYou chose: " + str(RPS(player)).replace("RPS.", ""))
print("Computer chose: " + str(RPS(computer)).replace("RPS.", ""))
if (player == 1 and computer == 3) | (player == 2 and computer == 1) | (player == 3 and computer == 2):

    print("🎉🎉🎉 You win! 🎉🎉🎉")
elif player == computer:
    print("😲 Tie Game!")
else:
    print("🐍 Python wins!")
