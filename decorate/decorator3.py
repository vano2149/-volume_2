"""
decorator.py file!
Page - > 522!
"""
calls = 0
def tracer(func):
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        print(f"Call {calls} to {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@tracer
def spam(a, b, c):
    print(a + b + c)

@tracer
def eggs(x, y):
    print(x ** y)

spam(1, 2, 3)
spam(a = 4, b = 5, c = 6)

eggs(1, 16)
eggs(4, y = 4)