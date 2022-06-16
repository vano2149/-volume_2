"""
call_decorators.py file!
Первый взгляд на декораторы функций,
определяемые пользователем!
страница 274!
"""


'''
class tracer:
    def __init__(self, func):
        """"""
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        """"""
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
'''

def tracer(func):
    """
    Реализация декоратора на замыкание!
    """
    def oncall(*args):
        oncall.calls += 1
        print(f"call {oncall.calls} to {func.__name__}")
        return func(*args)
    oncall.calls = 0
    return oncall

class C:
    @tracer
    def spam(self, a, b, c):
        return a + b + c
if __name__ == '__main__':
    x = C()
    print(x.spam(1,2,3))
    print(x.spam('a', 'b', 'c'))
