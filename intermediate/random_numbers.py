import random
import numpy as np

a = random.uniform(1, 100)
b = random.randint(1, 100)
c = random.randrange(1, 50)
print(a)
print(b)
print(c)

myList = list('ABCDEFGH')
random_choice = random.choice(myList)
random_sample = random.sample(myList, 3)
print(random_choice)
print(random_sample)
random.shuffle(myList)
print(myList)

# numpy: NumPy is a Python library used for working with arrays
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
arr = np.random.randint(0, 11, (3, 4))
np.random.shuffle(arr)
print(arr)
