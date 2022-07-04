"""
prop_deck_equiv.py file!
"""

class Property:
    """
    Данный класс содержит несколько функций!
    """
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance , instancetype = None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute!")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute!")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute!")
        self.fdel(instance)

class Person:
    def getName(self):
        print('getName...')
    def setName(self, value):
        print('setName...')
    name = Property(getName, setName)

if __name__ == '__main__':
    x = Person()
    x.name
    x.name = 'Bob'
    del x.name
