"""
extras.py file!
"""

def extra(self, arg): ...

class Extras(type):
    def __init__(Class, classname, superclasses, attributedict):
        if required():
            Class.extra = extra

class Client1(metaclass=Extras): ...
class Client2(metaclass=Extras): ...
class Client3(metaclass=Extras): ...

X = Client1()
X.extra()


def extra(self, arg): ...

def extras(Class):
    if required():
        Class.extra = extra
    return Class

class Client1: ...
Client1 = extras(Client1)

class Client2: ...
Client2 = extras(Client2)

class Client3: ...
Client3 = extras(Client3)

X = Client1()
X.extra()


def extra(self, arg): ...

def extras(Class):
    if required():
        Class.extra = extra
    return Class

@extra
class Client1: ...

@extra
class Client2: ...

@extra
class Client3: ...

X = Client1()
X.extra()
