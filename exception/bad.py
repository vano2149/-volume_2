"""
try_except_else.py file
Page -> Унифицированный синтаксис 
оператора try.
"""
def gobad(x,y):
    return x / y

def gosouth(x):
    print(gobad(x, 0))
'''
def kaboom(x,y):
    print(x + y)
try:
    kaboom([0, 1, 2], 'spam')
except TypeError:
    print('Hello World!')
print('resuming here')
'''

class MyError(Exception):
    pass
def stuff(file):
    raise MyError()

file = open('data', 'w')

try:
    stuff(file)
finally:
    file.close()
print('not reached')