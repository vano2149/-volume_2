"""
singleton.py file!
"""
instances = {}
'''
def singleton(aClass):
    """
    Версия №1!
    """
    def onCall(*args, **kwargs):
        if aClass not in instances:
            instances[aClass] = aClass(*args, **kwargs)
        return instances[aClass]
    return onCall


def singleton(aClass):
    """
    Альтернативная версия!
    """
    instance = None
    def onCall(*args, **kwargs):
        nonlocal instance
        if instance == None:
            instance = aClass(*args, **kwargs)
        return instance
    return onCall
'''

def singleton(aClass):
    """
    Версия №2!
    """
    def onCall(*args, **kwargs):
        if onCall.instance == None:
            onCall.instance = aClass(*args, **kwargs)
        return onCall.instance
    onCall.instance = None
    return onCall

class singleton:
    def __init__(self, aClass):
        self.aClass = aClass
        self.instance = None
    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.aClass(*args, **kwargs)
        return self.onCall

@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    
    def pay(self):
        return self.hours * self.rate

@singleton
class Spam:
    def __init__(self, val):
        self.attr = val
    
bob = Person('Bob Smith', 40, 10)
print(bob.name, bob.pay())

sue = Person('Sue Smith', 50, 10)
print(sue.name, sue.pay())

X = Spam(val=42)
Y = Spam(99)

print(X.attr, Y.attr)
