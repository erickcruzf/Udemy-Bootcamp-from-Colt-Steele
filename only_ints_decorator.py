from functools import wraps

def only_ints(fn):
    wraps(fn)
    def wrapper(*args):
        if any((arg for arg in args if type(arg) != int)): 
            return "Please only invoke with integers."
        return fn(*args)
    return wrapper
