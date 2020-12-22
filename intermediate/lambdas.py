# Lambda expressions (sometimes called lambda forms) are used to create anonymous functions
from functools import reduce


def add_func(x):
    return x + 10


# using lambda:
# add
print(lambda x: x + 10)
# multi
print(lambda x, y: x * y)

p2D = [(1, 2), (15, 1), (5, -1), (10, 4)]  # (x, y) points
p2d_sorted = sorted(p2D, key=lambda y: y[1])  # Sorted by Y index

print(p2D)
print(p2d_sorted)  # R/ [(5, -1), (15, 1), (1, 2), (10, 4)]

# map(func, seq)
myList = [1, 2, 3, 4, 5]
myListMapped = map(lambda x: x * 2, myList)
print(list(myListMapped))
# for this example. List Comprehension is simple and better
myListC = [x * 2 for x in myList]
print(myListC)

# filter(func, seq)
myListF = filter(lambda x: x % 2 == 0, myList)
print(list(myListF))
# We can achieve the same with List Comprehension

# reduce(func, seq)
# Apply a function of two arguments cumulatively to the items of a sequence, from left to right,
# so as to reduce the sequence to a single value
productList = reduce(lambda x, y: x * y, myList)
print(productList)
