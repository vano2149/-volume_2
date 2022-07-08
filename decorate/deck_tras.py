"""
deck_tras.py file!
"""

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f'Calls: {self.calls} to {self.func.__name__}')
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)
        return wrapper


class tracer:
    def __init__(self, meth):
        self.calls = 0
        self.meth = meth
    
    def __get__(self, instance, owner):
        def warpper(*args, **kwargs):
            self.calls += 1
            print(f'Calls {self.calls} to {self.meth.__name__}')
            return self.meth(*args, **kwargs)
        return warpper
