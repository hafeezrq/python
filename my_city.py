# Create a module in python

from random import choice

name = "Melbourne"
state = "Victoria"
country = "Australia"

def funfacts():
    facts = [
        "Melbourne is capital city of Victoria", "It is located East of Australia", "It is called sport capital of Australia", "MCG is in Melbourne"
    ]
    index = choice("0123")
    print(facts[int(index)])