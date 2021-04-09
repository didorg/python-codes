# Tuple: ordered, immutable, allows duplicate elements
# Some time can be more efficiently to work with Tuple since they are immutable (*1)
import sys

# (*1) -----------
my_list = [0, 1, 2, "Hello", True]
my_tuple = (0, 1, 2, "Hello", True)
print(sys.getsizeof(my_list), "bytes")  # R/ 120 bytes
print(sys.getsizeof(my_tuple), "bytes")  # R/ 80 bytes
