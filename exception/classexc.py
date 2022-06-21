"""
File classexc.py
"""

class General(Exception):
    pass

class Specific1(General):
    pass

class Specific2(General):
    pass

def raiser0():
    X = General()
    raise X

def raiser1():
    X = Specific1()
    raise X

def raiser2():
    X = Specific2()
    raise X

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:
        import sys
        print(f'cauting: {sys.exc_info()[0]}')

