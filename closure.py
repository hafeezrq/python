# Closure is function having access to the scope of its parent function after the parent function has returned

def function_parent(person):
    coins = 3

    # define the nested function
    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " hase " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " hase " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game


person1 = function_parent("Persone1")
person2 = function_parent("Person2")

# Following calls still work event function_parent has already returned, as these call still have access to the parent function variable. the same is true for method's params as well.
person1()
person1()
person1()

person2()
