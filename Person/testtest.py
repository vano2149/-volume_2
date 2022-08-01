"""
testtest.py file!
"""
def typetest(**argchecks):
    def onDecorator(func):
        ...
        def onCall(*pargs, **kargs):
            positionals = list(allargs)[:len(pargs)]
            for (argname, type) in argchecks.items():
                if argname in kargs:
                    if not isinstance(kargs[argname], type):
                        ...
                        raise TypeError(errmsg)
                    elif argname in positionals:
                        position = positionals.index(argname)
                        if not isinstance(pargs[position], type):
                            ...
                            raise TypeError(errmsg)
                    else:
            return func(*pargs, **kargs)
        return onCall
    return onDecorator

@typetest(a=int, c = float)
def func(a, b, c, d):
    ...
func(1, 2, 3.0, 4)
func('spam', 2, 99, 4)