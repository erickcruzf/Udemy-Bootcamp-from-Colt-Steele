from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def blocker(**kwargs):
        if any((kwarg for kwarg in kwargs.items() if kwarg[0] == 'role' and kwarg[1] == 'admin')):
            return fn(**kwargs)
        return "Unauthorized"
    return blocker
