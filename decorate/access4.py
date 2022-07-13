"""
access.py file!
"""

traceMe = False
def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args))+ ']')

class BuiltinsMixin:
    def __add__(self, other:str) -> None:
        """
        __add__ method -> str
        """
        return self.__class__.__getattr__(self, '__add__')(other)

    def __str__(self)-> str:
        """
        __str__method -> str
        """
        return self.__class__.__getattr__(self, '__str__')()

    def __getitem__(self, index:int) -> int:
        """
        __getitem__ method -> int
        """
        return self.class__.__getattr__(self, '__getitem__')(index)

    def __call__(self, *args, **kwargs)-> str:
        """
        __call__ method -> str
        """
        return self.__class__.__getattr__(self, '__call__')(*args, **kwargs)

    def accessControl(failIf):
        def onDecorator(aClass):
            class onInstance(BuiltinsMixin):
                def __init__(self, *args, **kwargs):
                    self.__wrapped = aClass(*args, **kwargs)
                
                def __getattr__(self, attr):
                    trace('Get: ' + attr)
                    if failIf(attr):
                        raise TypeError(f'Private attribute fetch : {attr}')
                    else:
                        return getattr(self.__wrapped, attr)
                
                def __setattr__(self, attr, value):
                    trace('Set: ', attr, value)
                    if attr == '_onInstance__wrapped':
                        self.__dict__[attr] = value
                    elif failIf(attr):
                        raise TypeError(f'Private attribute chenge: {attr}')
                    else:
                        setattr(self.__wrapped, attr, value)
            return onInstance
        return onDecorator

class BuiltinsMixin:
    def __add__(self, other):
        return self._wrapped + other
    def __str__(self):
        return str(self._wrapped)
    def __getitem__(self, index):
        return self.wrapped[index]
    def __call__(self, *args, **kwargs):
        return self._wrapped(*args, **kwargs)

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance(BuiltinsMixin):
            def __getattr__(self, attr):
                    trace('Get: ' + attr)
                    if failIf(attr):
                        raise TypeError(f'Private attribute fetch : {attr}')
                    else:
                        return getattr(self.__wrapped, attr)

            def __setattr__(self, attr, value):
                trace('Set: ', attr, value)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError(f'Private attribute chenge: {attr}')
                else:
                    setattr(self.__wrapped, attr, value)
        return onInstance
    return onDecorator

class BuiltinsMixin:
    def reroute(self, attr, *args, **kwargs):
        return self.__class__.__getattr__(self, attr)(*args, **kwargs)
    
    def __add__(self, other):
        return self.reroute('__add__',other)
    
    def __str__(self):
        return self.reroute('__str__')
    
    def __getitem__(self, index):
        return self.reroute('__getitem__', index)
    
    def __call__(self, *args, **kwargs):
        return self.reroute('__call__', *args, **kwargs)
