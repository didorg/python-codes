def foo(a, b, *args, **kwargs):  # *args is a tuple. **kwargs is a dictionary
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo(1, 2, 3, 4, 5, six=6, seven=7)


def boo(a, b, c):
    print(a, b, c)


my_list = (9, 6, 3)
boo(*my_list)

my_dictionary = {'a': 2, 'b': 4, 'c': 6}
boo(**my_dictionary)
