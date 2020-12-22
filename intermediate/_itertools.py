# itertools: product, permutations, combinations, accumulate, groupby, infinite iterators
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle, repeat

# product       --------------------------
# Cartesian product of input iterables
listA = [1, 2]
listB = [3]
prod = product(listA, listB)
print(list(prod))  # R/ [(1, 3), (2, 3)]

# permutations  --------------------------
# Return successive r-length permutations of elements in the iterable
listC = [2, 3, 4]
perm = permutations(listC)  # We can also specify the length of the permutation
print(list(perm))  # R/ [(2, 3, 4), (2, 4, 3), (3, 2, 4), (3, 4, 2), (4, 2, 3), (4, 3, 2)]

# combinations  --------------------------
# Return successive r-length combinations of elements in the iterable
comb = combinations(listC, 2)
print(list(comb))  # R/ Return successive r-length combinations of elements in the iterable

# accumulate    --------------------------
# Return series of accumulated sums (or other binary function results).
acc = accumulate(listC)
print(list(acc))  # R/ [2, 5, 9]

# groupby       --------------------------
# make an iterator that returns consecutive keys and groups from the iterable
animals = [("Pet", "cat"),
           ("Pet", "dog"),
           ("Bird", "peacock"),
           ("Bird", "pigeon")]
groupA = groupby(animals, lambda x: x[0])
for key, group in groupA:
    key_and_group = {key: list(group)}
    print(key_and_group)
    # R/    {'Pet': [('Pet', 'cat'), ('Pet', 'dog')]}
    #       {'Bird': [('Bird', 'peacock'), ('Bird', 'pigeon')]}

# infinite iterators --------------------------
# count()
for i in count(10):
    print(i)
    if i == 15:
        break

# cycle()
# Return elements from the iterable until it is exhausted. Then repeat the sequence indefinitely

# repeat()
# Create an iterator which returns the object for the specified number of times.
# If not specified, returns the object endlessly
