# Dictionary: Key-Value pairs, Unordered, Mutable
# Key. Can be any immutable type. has to be hashable type

# Creation
myDictionary = {"name": "Adam", "age": 25, "city": "NY"}
# Other way
myDictionary1 = dict(name="Adam", age=25, city="NY")
print(myDictionary)
print(myDictionary1)

# Accessing the values
name = myDictionary1['name']
print(name)

# Adding a value (since dictionaries are mutable, if the key exists, then is overridden)
myDictionary["email"] = "adam@gmail.cu"
print(myDictionary)

# Finding a value
try:
    print(myDictionary["d"])
except Exception as err:
    print("Oops! There is an error finding the Key: ", err)

# To iterate over the elements
for key in myDictionary:
    print(key)

for value in myDictionary.values():
    print(value)

for key, value in myDictionary.items():
    print(key, value)

# You can merge dictionaries with update().
dict1 = {1: 1, 2: 2, 3: 3}
dict2 = {1: 1, 2: 2, 3: 3, 4: 4}

dict1.update(dict2)  # R/ {1: 1, 2: 2, 3: 3, 4: 4}
print(dict1)
