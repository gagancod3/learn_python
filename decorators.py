# Timing function execution
# Write a decorator that measures and prints the execution time of a function.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        # *args and **kwargs to handle any number of arguments 
        start_time = time.time()  # Record start time

        result = func(*args, **kwargs)  # *Call the original function

        end_time = time.time()  # Record end time
        execution_time = end_time - start_time  # Calculate execution time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        
        return result  # Return the result of the original function
    return wrapper

@timer # *Applying the decorator*
def example_function(n):
    time.sleep(n)  # Simulate a function that takes n seconds to execute

example_function(2)  # Call the decorated function

# Output:
# Execution time of example_function: 2.0021 seconds


# Idea of decorators is that we can add functionality to existing functions
# without modifying their structure. We wrap the original function inside another function (the decorator).
# This is useful for cross-cutting concerns like logging, access control, and performance monitoring.
# Decorators are a powerful feature in Python that allow you to modify the behavior of a function or class.
# They are often used in web frameworks, logging libraries, and testing frameworks to add functionality in a clean and reusable way.
# They are applied using the @decorator_name syntax above the function definition.
# They can also be stacked to combine multiple decorators on a single function.




