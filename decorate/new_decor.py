"""
new_decor.py file!
"""

class Decorator:
    def __init__(self, C):
        self.C = C
    
    def __call__(self, *args):
        self.wrapped = self.C(*args)
        return self
    
    def __getattr__(self, attrname):
        return getattr(self.wraped, attrname)
    

@Decorator
class C:
    pass

x = C()
y = C()


def decorator(C):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = C(*args)
    return Wrapper

class Wrapper: ...
def decorator(C):
    def onCall(*args):
        return Wrapper(C(*args))
    return onCall
