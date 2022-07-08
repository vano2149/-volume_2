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

