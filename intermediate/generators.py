import sys


# generator functions are a special kind of function that returns some sort of lazy iterator.
# There are objects that you can loop over like a list, however, unlike lists,
# lazy iterators do not store their contents in memory.
# One of the advantages of generator functions to iterators is the amount of code that is required to code.

# Some use cases of generators are to optimize the performance of our python applications
# especially in scenarios when we work with large datasets or files

# There are two terms involved when we discuss generators.
# 1. Generator-Function : A generator-function is defined like a normal function,
# but whenever it needs to generate a value, it does so with the yield keyword rather than return.
# If the body of a def contains yield, the function automatically becomes a generator function.

# 2. Generator-Object : Generator functions return a generator object. Generator objects are used either by
# calling the next method on the generator object or using the generator object in a “for in” loop

# Normal func
def first_num(n):
    nums = []
    num = 0
    while num < n:
        nums.append(n)
        num += 1
    return nums


# Generator-Function
def first_num_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


# size of the normal func object in bytes
print(sys.getsizeof(first_num(1000000)))  # R/ 8448728 bytes
# size of the generator func object in bytes
print(sys.getsizeof(first_num_generator(1000000)))  # R/ 112 bytes


# A simple generator for Fibonacci Numbers
def fibonacci(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
fib = fibonacci(30)

# Iterating over the generator object using next
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

# Iterating over the generator object using for in loop.
for i in fib:
    print(i)
