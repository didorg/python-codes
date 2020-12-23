# Errors and Exceptions

# Exception: Common base class for all non-exit exceptions
x = 5
if x < 0:
    raise Exception('x should be positive')

# Assert statements are a convenient way to insert debugging assertions into a program:
# if not expression: raise AssertionError
num = 3
assert (num >= 0), 'num is not positive'

myDictionary = {"name": "Adam", "age": 25, "city": "NY"}
try:
    print(myDictionary["address"])
except Exception as err:
    print("Oops! There is an error finding the Key: ", err)

try:
    a = 5 / 1
    b = a + 'My String'
except TypeError as errType:
    print(errType)
except Exception as err:
    print(err)
else:
    print('All good!')
finally:
    print('cleaning up... ')


# -----------------------------------------
# Defining your own Exceptions
class ValueToHighError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def tes_value(v):
    if v > 10:
        raise ValueToHighError('value is to high', v)


try:
    tes_value(20)
except ValueToHighError as err:
    print(err.message, err.value)
# -----------------------------------------
