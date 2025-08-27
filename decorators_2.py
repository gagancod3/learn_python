# decorator example

def debug(func):
    def wrapper(*args, **kwargs):

        # storing arguments 
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}={v}" for k,v in kwargs.items())
        
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")

        return func(*args, **kwargs)
        
    return wrapper

@debug # *added Decorator
def greet(name,greeting="Hello",profession='Programmer'):
    print(f"{greeting}, {name}! I'm a {profession}")
    # return f"{greeting}, {name}!"

# calling the decorator 'debug' function
greet('Gagan',greeting='Hanji', profession='software engineer')

# decorator acts as a toll check where a function goes thorugh the decorator function to be executed.

# if we want to utilize debug function without the decorator syntax
# we can do this:

# wrapper_invoke = debug(greet)
# wrapper_invoke('Gagan',greeting='Hanji', profession='software engineer')

