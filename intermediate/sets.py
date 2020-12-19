# Sets: Unordered, mutable, no duplicates

mySet = {1, 2, 2, 3, 4, 5, 6}
print(mySet)  # R/ {1, 2}

mySet1 = set("Hello")
print(mySet1)  # R/ {'H', 'l', 'o', 'e'} / order is arbitrary and only one l.

# Empty Set
mySet2 = set()
# mySet2 = {} # This is a Dictionary.

mySet2.add("uno")
mySet2.add("dos")

# discard() does the same as remove(), but If the element is not a member, do nothing.
mySet2.discard("dos")
print(mySet2)
print(type(mySet2))

mySet3 = {5, 6, 7, 8, 9}

# union(): Return the union of sets as a new set
unionSet = mySet.union(mySet3)
print(unionSet)

# intersection(): Return the intersection of two sets as a new set.
iSet = mySet.intersection(mySet3)
print(iSet)

# difference(): Return the difference of two or more sets as a new set.
diffSet = mySet.difference(mySet3)
print(diffSet)

# symmetric_difference(): Return the symmetric difference of two sets as a new set
simDiffSet = mySet.symmetric_difference(mySet3)
print(simDiffSet)

# issubset() & issuperset()
print(mySet1.issubset(mySet))
print(mySet.issuperset(mySet3))

# ---------------------------------------------------------------------------------
# frozenset
# is an immutable version of a Set
imtSet = frozenset([9, 8, 7, 6, 5])
