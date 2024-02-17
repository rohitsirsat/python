import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def example_funtion(a, b):
    time.sleep(5)
    return a + b

print(example_funtion(3, 4))
print(example_funtion(3, 4))
print(example_funtion(4, 4))