# A Guess Number Game where Play guess a number

import sys
from random import choice

def guess_number_game(player_name):
    total_guesses = 0
    player_wins = 0

    player_guess = int(input(
        f"\n{player_name}, please guess a number between 1 and 3 inclusive\n"
    ))
    computer_guess = int(choice("123"))
    total_guesses += 1

    print(f"\n{player_name}, your guess: {player_guess}")
    print(f"\nComputer Guess: {computer_guess}")
    if player_guess == computer_guess:
        player_wins +=1
        print(f"\n{player_name} You win!")
    else:
        print(f"\nSorry! {player_name}, bad luck. Try next time.")
    print(f"\n Game Count: {total_guesses}")
    print(f"\n {player_name}' wins: {player_wins}")
    print(f"\n {player_name}'s success rate is {(player_wins/total_guesses)* 100}%.")

    sys.exit("Bye Bye")
    
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a personal greetings")

    parser.add_argument(
        "-n", "--name", 
        metavar="name", 
        required=True, 
        help="Name of the person to greet."
        )
    
    args = parser.parse_args()
    guess_number_game(args.name)