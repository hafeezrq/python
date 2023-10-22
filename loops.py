# Loope is Python

# A simply while loop
counter = 0
while counter < 10:
    print("Counter: " + str(counter))
    counter += 1

# while loope with "break"
aBreak = 0
while aBreak < 10:
    print("Break: " + str(aBreak))
    if aBreak == 5:
        break
    aBreak += 1

# while loope wiht "continue"
aContinue = 0
while aContinue < 10:
    aContinue += 1
    if aContinue == 5:
        continue
    print("Continue: " + str(aContinue))

# while / else
anElse = 0
while anElse < 10:
    print("Else: " + str(anElse))
    anElse += 1
else:
    print("Awsome Else! " + str(anElse))

##########################################

# for/in loop
names = ["Shaarif", "Breeah", "Zuhair"]
for name in names:
    print(name)

# loope through a string
for char in "Melbourne":
    print(char)
print("")

# for loop with break
for name in names:
    if name == "Zuhair":
        break
    print(name)

print("")

# for loop with continue
for name in names:
    if name == "Breeah":
        continue
    print(name)

print("")

# neted loops
doos = ["Homework", "Eat", "Sleep"]
for name in names:
    print("\n" + name)
    for does in doos:
        print(does)
print("")

# Loop through a range of numbers
for x in range(5):
    print(x)

print("")
# Loop through a range Start and End

for x in range(3, 7):
    print(x)

print("")
# Loop through a Range Increment Value
for x in range(0, 101, 10):
    print(x)

print("")
# for loop with else
for x in range(0, 101, 10):
    print(x)
else:
    print("Glad that ended!")
