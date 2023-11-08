import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPPER = 2
    SCISSORS = 3


def rps(player_name="Player01"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_name
        nonlocal player_wins
        nonlocal python_wins

        playerchoice = input(
            f"\n{player_name}, please enter...\n1 for Rock\n2 for Paper\n3 for Scissor:\n")
        player_choice = int(playerchoice)

        machine_choice = int(random.choice("123"))

        if player_choice < 1 or player_choice > 3:
            sys.exit(f"{player_name}, please enter 1 or 2 or 3")
        print(
            f"\n{player_name}, you chose:  {(str(RPS(player_choice))).replace('RPS.', '').title()}")
        print(
            f"Computer chose: {(str(RPS(machine_choice))).replace('RPS.', '').title()}")

        # Use nested within nested function
        def decide_winner(player, computer):
            nonlocal player_name
            nonlocal player_wins
            nonlocal python_wins
            if (player == 1 and computer == 3) | (player == 2 and computer == 1) | (player == 3 and computer == 2):
                player_wins += 1
                return f"\n🎉🎉🎉 {player_name}, You win! 🎉🎉🎉\n"
            elif player == computer:
                return "\n😲😲😲😲😲 Tie Game!😲😲😲😲😲\n"
            else:
                python_wins += 1
                return "\n🎉🎉🎉  🐍 Computer wins! 🎉🎉🎉\n"

        game_result = decide_winner(player_choice, machine_choice)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"Game Count: {(game_count)}")
        print(f"{player_name} wins: {(player_wins)}")
        print(f"Computer wins: {(python_wins)}")
        print(f"\n{player_name}Play again?")

        while True:
            play_again = input(f"\nY for yes | Q for Quit: ")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
                return play_rps()
        else:
            print("\n🎉🎉🎉🎉🎉🎉🎉🎉🎉")  
            print(f"\n{player_name}, Thanks for playing!")   
            sys.exit(f"\n{player_name} Bye Bye!")

    return play_rps

# Just to prevent it from execution at the import time
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a personalized game experience!")

    parser.add_argument(
        "-n", "--name", 
        metavar="name", 
        required=True, 
        help="Name of the player."
        )
    
    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()