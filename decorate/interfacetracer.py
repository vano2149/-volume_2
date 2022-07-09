"""
decorclass.py file!
Page -> 542!
"""

def Tracer(aClass):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetches = 0
            self.wrapped = aClass(*args, **kwargs)
        
        def __getattr__(self, attrname):
            print(f'Trace: {attrname}')
            self.fetches += 1
            return getattr(self.wrapped, attrname)
    return Wrapper

if __name__ == '__main__':
    @Tracer
    class Spam:
        def display(self):
            print('Spam!' * 8)
    
    @Tracer
    class Person:
        def __init__(self, name, hours, rate):
            self.name = name
            self.hours = hours
            self.rate = rate
        def pay(self):
            return self.hours * self.rate

if __name__ == '__main__':
    food = Spam()
    food.display()
    print([food.fetches])

    bob = Person('Bob Smith', 40, 50)
    print(bob.name)
    print(bob.pay())

    print('')
    sue = Person('Sue Jones', rate=100, hours=60)
    print(sue.name)
    print(sue.pay())

    print(bob.name)
    print(bob.pay())
    print([bob.fetches, sue.fetches])
