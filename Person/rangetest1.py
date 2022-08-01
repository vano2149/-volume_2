"""
rangetest1.py file!
Page -> 567!
"""

def rangetest(*argchecks):

    def onDecorator(func):
        if not __debug__:
            return func
        else:
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = f'Argument {ix} not in {low}..{high}'
                    raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator
