# Dictionary in Python (key:value)

# Creat Dictionary
band = {
    "Vocals": "Plant",
    "Guitar": "Page"
}

# Or by using constructor function
band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)

# Try methods
print(type(band))
print(type(band2))

print(len(band))

# Accesss Items
print(band["Vocals"])
print(band2.get("guitar"))

# List all keys
print(band.keys())

# List all values
print(band.values())

# List of key/value pairs as tuple
print(band.items())

# Verify a key exists
print("Guitar" in band)
print("NotKey" in band)

# Change values
band["Vocals"] = "Coverdale"  # Change an existing value
print(band)

band.update({"Bass": "JPJ"})  # Adds new key/value in dictionary
print(band)

# Remove/Delete a key/value
print(band.pop("Bass"))
print(band)

band["Drums"] = "Bonham"
print(band)
# popitem() removes the most recent item and return tuple.
print(band.popitem())
print(band)

# Delete(del) and clear()
band["Drums"] = "Bonham"
print(band)
del band["Drums"]
print(band)
band2.clear()  # Clear dictionary
print(band2)
del band2  # Delete dictionary

# Copy dictionary
band2 = band  # Not a copy. Just refer to the same dict
band2["Bass"] = "JPJ"
print("It is a bad copy!")
print(band)
print(band2)

# use copy() to copy a dict
band2 = band.copy()
band2["Drums"] = "Bonham"
print("\nThis is good copy")
print(band)
print(band2)

# or use dict() constructor method to copy
band3 = dict(band)
print(band3)

####### Nested Dictionaries ############
member1 = {
    "name": "Member1",
    "instrument": "vocals"
}

member2 = {
    "name": "Member2",
    "instrument": "guitar"
}

maindict = {
    "member1": member1,
    "member2": member2
}
print(maindict)

# Access memeber in nested dictionay
print(maindict["member1"]["name"])
