# Importing and using builtin and custom module in python

# import a module
import math 

# import a member of module
from random import choice

# import and give it alias
import enum as enm

# import your custome module
import my_city

from rps import rock_paper_scissors

print(math.pi)
print(choice('12345'))
print(enm.__name__)
print("\n" + my_city.name)
my_city.funfacts()

# module name
print(__name__)
print(my_city.__name__)

# play rock_paper_scissors
rock_paper_scissors()