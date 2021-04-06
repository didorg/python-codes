# List Comprehension *************************************************************
nums = [1, 2, 3, 4, 5, 6, 7, 8]

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
