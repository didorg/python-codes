# List Comprehension *************************************************************
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]

# I want 'n*n' for each 'n' in nums
# Normal for
# my_list = []
# for n in nums:
#     my_list.append(n * n)
# print(my_list)

# With List Comprehension
nums_lc = [n * n for n in nums]
print(nums_lc)

# I want 'n*n' for each 'n' in nums
# Normal for
# evens = []
# for n in nums:
#     if n % 2 == 0:
#         evens.append(n)
# print(evens)

# With List Comprehension
evens_lc = [n for n in nums if n % 2 == 0]
print(evens_lc)

# Dictionary Comprehension *******************************************************
# I want a dict{'name': 'hero'} for each name, hero in zip(names, heroes)
names = ['Bruce', 'Peter', 'John']
heroes = ['Batman', 'Superman', 'Wolverine']

# Normal for loop
# my_dict = {}
# for name, hero in zip(names, heroes):
#     my_dict[name] = hero
# print(my_dict)

# # Dict Comprehension
heroes_dict = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
print(heroes_dict)

# Set Comprehension ***************************************************************
my_set = {n * n for n in nums}
# print(type(my_set)) R/ <class 'set'>
print(my_set)  # R/ {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}

# Generators Comprehension ***************************************************************
# def gen_func(nums):
#     for n in nums:
#         yield n * n
#
# my_gen = gen_func(nums)

my_gen = (n * n for n in nums)
# print(type(my_gen)) R/ <class 'generator'>

for i in my_gen:
    print(i)
