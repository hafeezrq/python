# Accepting and Using Command Line Arguments

import argparse

parser = argparse.ArgumentParser(description="Provides a personal greetings")

parser.add_argument(
    "-n", "--name", 
    metavar="name", 
    required=True, 
    help="Name of the person to greet."
    )
args = parser.parse_args()
message = f"Hello {args.name}!"
print(message)
