"""
call_decorators.py file!
Первый взгляд на декораторы функций,
определяемые пользователем!
страница 274!
"""

class tracer:
    def __init__(self, func):
        '''
        '''
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        '''
        '''
        self.calls += 1
        print(f'Call {self.calls, self.func.__name__}')
        return self.func(*args)
   
@tracer
def spam(a, b ,c):
    """
    """
    return a + b + c

print(spam(1,2,3))
print(spam('a', 'b', 'c'))
