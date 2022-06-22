"""
except_finally.py file!
page -> 380.
Идиомы исключений!
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
