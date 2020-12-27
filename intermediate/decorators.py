import functools


# Decorators are functions that modify other functions’ behaviors without changing their core operations
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for n in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')


greet('Dido')
