# Tuple: ordered, immutable, allows duplicate elements
# Some time can be more efficiently to work with Tuple since they are immutable (*1)
import sys
import timeit

myTuple = ("Name", 25, "NJ")  # Parenthesis are optionals
print(myTuple)

# You can use tuple function to create a tuple from iterable, exp:
myTupleFromFunction = tuple(["Name", 22, "NY"])
print(myTupleFromFunction)

# Convert to a list
myList = list(myTuple)
print(myList)

# Unpacked
name, age, city = myTuple
print(age)

myNumberTuple = (1, 2, 3, 4, 5, 6)
i1, *i2, i3 = myNumberTuple
print(i1)  # R/ 1
print(i2)  # R/ [2, 3, 4, 5]
print(i3)  # R/ 6

# (*1) -----------
demoList = [0, 1, 2, "Hello", True]
demoTuple = (0, 1, 2, "Hello", True)
print(sys.getsizeof(demoList), "bytes")
print(sys.getsizeof(demoTuple), "bytes")

# (*1) -----------
#  --- timeit tool for measuring execution time of small code snippets.
# Create a List one million time
print(timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000))  # R/ 0.049025797
# Create a Tuple one million time
print(timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000))  # R/ 0.006612965999999998
