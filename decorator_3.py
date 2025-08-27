# Cache return values
import time

def cache(func):
    cache_val = {}
    print(cache_val)
    def wrapper(*args, **kwargs):
        if args in cache_val:
            return cache_val[args]
        
        result = func(*args)
        cache_val[args]= result

        return result
    return wrapper

@cache
def long_running_fn(a,b):
    time.sleep(4)
    return a + b


print(long_running_fn(1,2))
print(long_running_fn(1,2))
print(long_running_fn(3,2))

