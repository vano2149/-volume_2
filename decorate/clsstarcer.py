"""
clsstracer.py file!
Page -> 546
"""

class Tracer:
    def __init__(self, aClass):
        self.aClass = aClass

    def __call__(self, *args):
        self.wrapped = self.aClass(*args)
        return self

    def __getattr__(self, attrname):
        print(f'Tracer: {attrname}')
        return getattr(self.wrapped, attrname)

@Tracer
class Person:
    def __init__(self, name):
        self.name = name
if __name__ == '__main__':
    bob = Person('Bob')
    print(bob.name)
    Sue = Person('Sue')
    print(Sue.name)
    print(bob.name)