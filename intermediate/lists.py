# Lists: ordered, mutable, allows duplicate elements
from intermediate.utils.person import Person

myList = ['apple', 'mango', 'cherry']

print(myList)

if 'mango' in myList:
    print('yes')
else:
    print('No')

print(len(myList))

# Append object to the end of the list.
myList.append('guava')
print(myList)

# Insert object before index
myList.insert(1, "blueberry")
print(myList)

lastItem = myList.pop()
print(lastItem)
print(myList)

# Sort the original list in ascending order
# myList.sort()
# print(myList)

# Return a new list containing all items from the iterable in ascending order.
s_list = sorted(myList)
print(s_list)

# Sort obj list --------------------------
p1 = Person('Anne', 'Musk', 25)
p2 = Person('Peter', 'Glez', 31)
p3 = Person('Mari', 'Lu', 28)
person_list = [p1, p2, p3]

# for more complicated sort...
# def p_sort(p):
#     return p.age

print('Sorted by name')
s_p_list = sorted(person_list, key=lambda p: p.age, reverse=True)
print(s_p_list)
# ----------------------------------------

multi_List = [1] * 3
num_list = [0, 2, 3]
print(multi_List)

concat_list = multi_List + num_list
print(concat_list)

# ------ Slicing for Lists ------
# Slicing is a flexible tool to build new lists out of an existing list.
# It's creates a shallow copy of the initial list. That means, we can safely modify the new list and it will not affect
# the initial list. The full slice syntax is:
# start:stop:step
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# We did not use step in our slice, so we did not skip any element and obtained all values within the range.
# Here we start from the first element(index 0) and take a list till the element with index 4.
a = numbers[0:4]
print(a)

# Slice notation allows you to skip any element of the full syntax. If we skip the start number then it starts from 0
b = numbers[:3]  # is equivalent to nums[0:3]
print(b)

# Negative indexes allow us to easily take n-last elements of a list:
last_numbers = numbers[-3:]  # Result: [6, 7, 8]
n_numbers = numbers[-3:7]
print(last_numbers)
print(n_numbers)

# Step parameter. Taking every nth-element of a list
step_numbers1 = numbers[::2]  # Result: [1, 3, 5, 7]
print(step_numbers1)
step_numbers2 = numbers[1::2]  # Result: [2, 4, 6, 8]
print(step_numbers2)

# If we don’t want to include some elements at the end, we can also add the stop parameter:
step_numbers3 = numbers[1:-3:2]  # Result: [2, 4] -> stop -3 pos, which is number 6.
print(step_numbers3)

# Reverse whit Step -> start:stop:step
# Negative step changes a way, slice notation works. It makes the slice be built from the tail of the list
r = numbers[::-1]
print(r)

# ------ Slice Object ---
# https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/#Slice_Object

# Copy Original List
copy1 = numbers.copy()  # Result: [1, 2, 3, 4, 5, 6, 7, 8]
copy2 = numbers[:]  # Result: [1, 2, 3, 4, 5, 6, 7, 8]
copy3 = list(numbers)  # Result: [1, 2, 3, 4, 5, 6, 7, 8]
