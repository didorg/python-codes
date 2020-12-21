# Strings: Ordered, Immutable, Text representation
from timeit import default_timer as timer

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

# ---------------------------------------------------------------
# Split(): Return a list of the words in the string, using sep as the delimiter string. Other you have to specified
myList = myString.split()
print(myList)

myStr = "Hola Mundo, Python is great!"
myStrList = myStr.split(",")
print(myStrList)

strL = ['How', 'are', 'you', 'doing']
nString = " ".join(strL)
print(nString)

# join(): Concatenate any number of strings. ----------------------
myListTime = ['a'] * 1000000

# bad code to concatenate: default_timer(timer()) for demonstration
start = timer()
my_String = ''
for s in myListTime:
    my_String += s
stop = timer()
print(stop - start)  # R/ 0.173672637

# good code to concatenate: default_timer(timer()) for demonstration
start = timer()
my_String = ''.join(myListTime)
stop = timer()
print(stop - start)  # R/ 0.00625867400000002

# Formatting Strings ------------------------------------------------
# %
# .format()
# since Python 3.6: f-String
var = 'Tom'
varPi = 3.14159

myStringOldFormat = "The variable is %s" % var  # s: String, d: decimal, f: float (ex: %.2f -> x.xx) ...etc.
myStringFormat = "The variable is {:.2f} and {}".format(varPi, var)  # {} default
myStringNewStyleFormat = f"The variable is {var} and {varPi}"  # Faster than old styles

print(myStringOldFormat)
print(myStringFormat)
print(myStringNewStyleFormat)

