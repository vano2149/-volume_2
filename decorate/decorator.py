"""
decorator.py file!
"""

"""
class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print(f'Call {self.calls} to {self.func.__name__}')
        self.func(*args)

@Tracer
def spam(a, b, c):
    print(a + b + c)

spam(1, 2, 3)
"""
class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f'Call {self.calls} to {self.func.__name__}')
        return self.func(*args, **kwargs)

@Tracer
def spam(a, b, c):
    print(a + b + c)

@Tracer
def eggs(x, y):
    print(x ** y)

if __name__ == '__main__':
    spam(1, 2, 3)
    spam(a=4, b=5, c=6)
    eggs(2, 16)
    eggs(4, y=4)
