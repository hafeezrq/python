
########### Functions in Python ################

# Function definition
def hello_world():
    print("Hello World!")


# Function call
hello_world()

# Function with parameter(s)


def sum(number1, number2):
    print(number1 + number2)


sum(3, 5)
sum(100, 498)

# function wiht default value(s)
# Note: a non-default can't follow a parameter with default
def afunc(num1=5, num2=3):
    print(num1 + num2)


afunc()

# Function with return statement
def return_func(x, y):
    return x + y


total = return_func(45, 45)
print(total)

# Function with variable number of arguments
# This * will make arguments into tuple.
def multi_args_func(*args):
    print(args)
    print(type(args))
    print("===============")


multi_args_func("Dave", "John", "Sarah")

# Function with named/keywords arguments
# ** will make arguments/data into a dictinary
def multi_named_args_func(**kwargs):
    print(kwargs)
    print(type(kwargs))


multi_named_args_func(first="Dave", last="Gray")
