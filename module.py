# Importing and using module in python

# import a module
import math 

# import a member of module
from random import choice

# import and give it alias
import enum as enm

# import your own module
import my_city

print(math.pi)
print(choice('12345'))
print(enm.__name__)
print("\n" + my_city.name)
my_city.funfacts()

# module name
print(__name__)
print(my_city.__name__)