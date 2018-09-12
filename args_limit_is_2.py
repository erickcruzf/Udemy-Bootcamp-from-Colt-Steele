from functools import wraps

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def three_args(*args):
        if len(args) > 2:
            return "Too many arguments!"
        return fn(*args)
    return three_args
