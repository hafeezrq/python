import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPPER = 2
    SCISSORS = 3


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        playerchoice = input(
            "\nEnter...\n1 for Rock\n2 for Paper\n3 for Scissor:\n")
        player = int(playerchoice)

        machinechoice = random.choice("123")
        computer = int(machinechoice)

        if player < 1 or player > 3:
            sys.exit("You must enter 1 or 2 or 3")
        print("\nYou chose: " + str(RPS(player)).replace("RPS.", ""))
        print("Computer chose: " + str(RPS(computer)).replace("RPS.", ""))

        # Use nested within nested function
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if (player == 1 and computer == 3) | (player == 2 and computer == 1) | (player == 3 and computer == 2):
                player_wins += 1
                return "\n🎉🎉🎉 You win! 🎉🎉🎉\n"
            elif player == computer:
                return "\n😲😲😲😲😲 Tie Game!😲😲😲😲😲\n"
            else:
                python_wins += 1
                return "\n🎉🎉🎉  🐍 Python wins! 🎉🎉🎉\n"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print("Game Count: " + str(game_count))
        print("Player wins: " + str(player_wins))
        print("Computer wins: " + str(python_wins))
        play_again = input("\nPlay again?: Y for yes | N for no: ")
        if play_again.lower() == "y":
            play_rps()
        sys.exit("Bye Bye!")

    return play_rps


play = rps()
play()
