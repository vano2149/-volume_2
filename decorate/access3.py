"""
access3.py file!
"""

from decorate.access2 import trace

traceMe = False
def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args))+ ']')

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.__wrapped = aClass(*args, **kwargs)

            def __str__(self):
                return str(self.__wrapped)

            def __add__(self, other):
                return self.__wrapped + other

            def __getitem__(self, index):
                return self.__wrapped[index]

            def __call__(self, *args, **kwargs):
                return self.__wrapped(*args, **kwargs)

            def __getattr__(self, attr):
                trace('Get: ', attr)
                if failIf(attr):
                    raise TypeError(f'Private attribute fetch: {attr}')
                else:
                    return getattr(self.__wrapped, attr)
                
            def __setattr__(self, attr, value):
                trace('Set: ', attr, value)
                if attr =='_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failIf:
                    raise TypeError(f'Private attribute change: {attr}')
                else:
                    setattr(self.__wrapped, attr, value)
        return onInstance
    return onDecorator

