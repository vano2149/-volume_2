"""
addr.py file!
Page -> 505!
"""
class decorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args):
        self.func(*args)
    
@decorator
def func(x, y):
    return print(x, y)


class C:
    @decorator
    def method(x, y):
        ...


