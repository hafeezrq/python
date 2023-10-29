import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPPER = 2
    SCISSORS = 3


game_count = 0


def rps():

    playerchoice = input(
        "\nEnter...\n1 for Rock\n2 for Paper\n3 for Scissor:\n")
    player = int(playerchoice)

    machinechoice = random.choice("123")
    computer = int(machinechoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1 or 2 or 3")
    print("\nYou chose: " + str(RPS(player)).replace("RPS.", ""))
    print("Computer chose: " + str(RPS(computer)).replace("RPS.", ""))

    # Use nested function
    def decide_winner(player, computer):
        if (player == 1 and computer == 3) | (player == 2 and computer == 1) | (player == 3 and computer == 2):
            return "🎉🎉🎉 You win! 🎉🎉🎉\n"
        elif player == computer:
            return "😲😲😲😲😲 Tie Game!😲😲😲😲😲\n"
        else:
            return "🎉🎉🎉  🐍 Python wins! 🎉🎉🎉\n"

    game_result = decide_winner(player, computer)
    print(game_result)

    # This is how you modify the global variable in python
    global game_count
    game_count += 1
    # global variable modified above!
    print("Game Count: " + str(game_count))
    play_again = input("Play again?: Y for yes | N for no: ")
    if play_again.lower() == "y":
        rps()
    sys.exit("Bye Bye!")


rps()
