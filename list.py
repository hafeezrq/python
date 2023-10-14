# Demo List data in Python

users = ["Dave", "John", "Sara"]

data = ["Dave", 55, "Melbourne"]

emptyList = []

# Test existence of list element
# print("Dave" in users)
# print("Dave" in data)
# print("Dave" in emptyList)

# A list element at a certain index
# print(users[0])
# print(data[2])
# print(users[-1])  # Last index
# print(users[-2])  # 2nd Last index

# Get index of an element in a list
# print(users.index("John"))

# Get a range of elements in a list
# Exclusive of the second number as does not include the element at the index 2.
# print(users[0:2])
# print(users[1:])  # Includes the element at 1 to the end of the list

# print(users[-3:-1])  # Get the elements from -3 to -2. -1 exclusive = [0:2]

# Get the length of the list
# print(len(data))

# Append an element at the end of the list
users.append("Eliza`")
# print(users)

# Add an element at th start of the list
users.insert(0, "Bob")
# print(users)

# Add two lists together
users += ["Jason", "Mary"]
# print(users)

# Alternatively you can add lists as follows
users.extend(["Robert", "Jimmy"])  # Or can give an exsisting list as argument
# print(users)

# Add elments from a certain index without replacing the existing ones
users[2:2] = ["Edie", "Alex"]
print(users)

# Replace the existing element from a certain index to exclusive other range no.
users[1:3] = ["Robby", "William", "test1", "test2"]
print(users)

# Remove an element from the list
users.remove("test1")
print(users)

# Remove and return the last elment in the list
print(users.pop())
print(users)

# Delete an element from a certain index
del users[3]
print(users)

# Delete all elements from a list
data.clear()
print(data)

# Delete who list
# del data
# print(data)
print("################################")

# Sort a list
users.sort()
print(users)

# Note all element starts with capital letters, add an element with small
users[2:2] = ["test"]
print(users)
users.sort()
# Note that the element with the small letter start is put at the end
print(users)

# Following will put the element in it right place in the order
users.sort(key=str.lower)
print(users)

print("*************************************")

# Use a number list to demo different methods

num_list = [4, 42, 78, 1, 5]
print(num_list)

# Reverse the order of the list index-wise
num_list.reverse()
print(num_list)

# Ascending Sort
num_list.sort()
print(num_list)

# Descending sort
# num_list.sort(reverse=True)
# print(num_list)

# Use global sort method to sort without changing the original list
print(sorted(num_list, reverse=True))
print(num_list)

# Methods to copy a list
num_list_copy = num_list.copy()  # copy Method
my_num_list = list(num_list)  # list constructor method
my_list_copy = num_list[:]  # all elements copy to new list

print(num_list_copy)
print(my_num_list)
my_list_copy.sort(reverse=True)
print(my_list_copy)
print(num_list)

# Test the type
print(type(num_list))

# Create a list using constructor
mylist = list([1, "Neil", "True"])
print(mylist)
