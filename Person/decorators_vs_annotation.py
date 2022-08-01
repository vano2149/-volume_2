"""
decorators_vs_annotation.py file!
"""

def rangetest(**argchecks):
    def onDecorator(func):
        def onCall(*pargs, **kwargs):
            print(argchecks)
            for check in argchecks:
                pass
            return func(*pargs, **kwargs)
        return onCall
    return onDecorator

@rangetest(a=(1, 5), c=(0.0, 1.0))
def func(a,b,c):
    print(a + b + c)

func(1,2, c=3)


def rangetest(func):
    def onCall(*pargs, **kwargs):
        argchecks = func.__annotations__
        print(argchecks)
        for check in argchecks:
            pass
        return func(*pargs, **kwargs)
    return onCall

@rangetest
def func(a:(1, 5) , b, c:(0.0, 1.0)):
    print(a + b + c)
func(1, 2, c=3)