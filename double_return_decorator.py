#Retorna qualquer função duas vezes em uma lista.
from functools import wraps

def double_return(fn):
    @wraps(fn)
    def double(*args,**kwargs):
        return [fn(*args, **kwargs), fn(*args, **kwargs)]
    return double
