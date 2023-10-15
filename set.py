############ Set Datastructure ##############

# Create a set
number_set = {1, 2, 3, 4, }

# Or using constructor
number_set2 = set((5, 6, 7, 8))

print(number_set)
print(number_set2)
print(type(number_set))
print(type(number_set2))
print(len(number_set))

# Duplicate not allowed in set
dupe_set = {1, 2, 2, 3, 4}
print(dupe_set)

# True is dupe to 1, False is dupe to 0
dupe_set = {1, True, 2, 3, False, 6, 7, 0}
# Note it take the first value of dupes
print(dupe_set)

# Check existance of value in a set
print(2 in number_set)
print(9 in number_set)

# Add new element in a set
number_set.add(5)
print(number_set)

# Add element of a set to another set
number_set.update(dupe_set)
print(number_set)

# Merge two sets to a new set
set1 = {1, 2, 3}
set2 = {2, 3, 4, 5, 6}
newset = set1.union(set2)  # union takes only distinct elements.
print(newset)

# intersection takes same elements
newset = set1.intersection(set2)
print(newset)

# Keep every element except dupes
set1 = {1, 2, 3}
set2 = {2, 3, 4, 5, 6}
newset = set1.symmetric_difference(set2)
print(newset)

# intersection_update and symmetric_difference_update changes the set for being called
