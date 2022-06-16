"""
Привер написания декоратора
класса!
"""

def count(aClass):
    """"""
    aClass.numInstances = 0
    return aClass

@count
class Spam:
    pass

@count
class Sub(Spam):
    pass

@count
class Other(Spam):
    pass


def decorator(cls):
    """
    Пример написания декоратора!
    """
    class Proxy:
        def __init__(self, *args):
            self.wrapped = cls(*args)
        def __getattr__(self, name):
            return getattr(self.wraped, name)
    return Proxy

@decorator
class C:
    ...
x = C()