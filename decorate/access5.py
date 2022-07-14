"""
access5.py file!
"""
traceMe = False
def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args))+ ']')


def accessControl(failIf):
    def onDecorator(aClass):
        def getattributes(self, attr):
            trace('Get:' + attr)
            if failIf(attr):
                raise TypeError(f'Privale attribute fetch: {attr}')
            else:
                return object.__getattribute__(self, attr)
        def setattributes(self, attr, value):
            trace('Set:' + attr)
            if failIf(attr):
                raise TypeError(f'Private attribute change {attr}')
            else:
                return object.__setattr__(self, attr, value)
        aClass.__getattribute__ = getattributes
        aClass.__setattr__ = setattributes
        return aClass
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))

if __name__ == '__main__':
    @Private('age')
    class Person:
        """
        Doc String a Person class!
        """
        def __init__(self, name, age):
            self.name = name
            self.age = age

    X = Person('bob smith', 40)
    print(f"Hi my name is {X.name.title()}!")
