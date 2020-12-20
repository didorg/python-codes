# Strings: Ordered, Immutable, Text representation

# Strings can use slicing operator just like Lists. See lists.py inside this package
myString = "Hello Word"
mySubString = myString[1:5]  # R/ ello
print(mySubString)

# strip(): Return a copy of the string with leading and trailing whitespace removed
myString1 = "  Hello   "
myString1 = myString1.strip()
print(myString1)

# Upper and Lower
print(myString.upper())
print(myString.lower())

print(myString.count('o'))
print(myString.lower().startswith('h'))

# Split(): Return a list of the words in the string, using sep as the delimiter string. Other you have to specified
myList = myString.split()
print(myList)

myStr = "Hola Mundo, Python is great!"
myStrList = myStr.split(",")
print(myStrList)

