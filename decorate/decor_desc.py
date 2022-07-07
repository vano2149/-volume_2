"""
decor_desc.py file!
"""

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f'Calls {self.calls} to {self.func.__name__}')
        return self.func(*args, **kwargs)
    
    def __get__(self,  instance, owner):
        return wrapper(self, instance)

class wrapper:
    def __init__(self, desc, subj):
        self.desc = desc
        self.subj = subj
    
    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)
    
@tracer
def spam(a, b, c):
    print(a + b + c)

@tracer
def eggs(N):
    return 2 ** N

class Person:
    def __init__(self, name , pay):
        self.name = name
        self.pay = pay
    
    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    
    @tracer
    def lastName(self):
        return self.name.split()[-1]
    
if __name__ == '__main__':
    spam(1, 2, 3)
    spam(a=4, b=5, c=6)
    print(eggs(32))
    print('-' * 20)
    print('methods...')
    bob = Person('Bob Smith', 50000)
    sue = Person('Sue Jones', 100000)
    print(bob.name, sue.name)
    sue.giveRaise(.10)
    print(int(sue.pay))
    print(bob.lastName(), sue.lastName())
    