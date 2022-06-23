"""
except_finally.py file!
page -> 384.
Отладка с помощью внешних операторов try
"""

def raise1():
    raise IndexError

def noraise():
    return

def raise2():
    raise SyntaxError

for func in (raise1, noraise, raise2):
    print(f'{func.__name__}')
    try:
        try:
            func()
        except IndexError:
            print('caugth IndexError')
    finally:
        print('Finally run')
    print('...')
