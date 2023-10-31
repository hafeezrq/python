# Old and new ways to concatanate and format strings in python

name = "Dave"
coins = 3

# + opetator to concatanation
message = "\n" + name + " has " + str(coins) + " coins left." + " (+ operator)"
print(message)

# Formatting with %
message = "\n%s has %s coins left. (%% operator)" % (name, coins)
print(message)

# .format method
message = "\n{} has {} coins left. (.format method)".format(name, coins)
print(message)

message = "\n{1} has {0} coins left. (.format method using index)".format(
    coins, name)
print(message)

message = "\n{name} has {coins} coins left. (.format method usin variables)".format(
    name=name, coins=coins)
print(message)

player = {'name': 'Dave', 'coins': 3}
message = "\n{name} has {coins} coins left. (.format method using dictionary)".format(
    **player)
print(message)

###############################

# f-Strings! The latest way to do strings
message = f"\n{name} has {coins} coins left. (f-string)"
print(message)

message = f"\n{name} has {1 * 3} coins left. (f-string using maths equation.)"
print(message)

message = f"\n{name.upper()} has {1 * 3} coins left. (f-string using string method.)"
print(message)

message = f"\n{player['name']} has {player['coins']} coins left. (f-string using dictionary.)"
print(message)

number = 10
print(
    f"\n2.25 times {number} is {2.25 * number:.2f} f-string using format options")

print("\n f-String in loop")
for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")
