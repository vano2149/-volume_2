"""
"""

def action2():
    print(1 + [])
"""
def action1():
    try:
        action2()
    except TypeError:
        print('inner try')
try:
    action1()
except TypeError:
    print('outher try')
"""

try:
    try:
        action2()
    except TypeError:
        print('inner try')
except TypeError:
    print('outer try')

try:
    try:
        raise IndexError
    finally:
        print('spam')
finally:
    print('SPAM')
