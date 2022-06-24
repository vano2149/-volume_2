"""
file oops.py
Page -> 406!
Unicode and bytes list!
Time code 1:39:05
"""

class Oops(Exception):
    """"""
    def MyError():
        raise Exception("MyError")

def oops():
    """"""
    raise IndexError

def oops1():
    return oops()
try:
    oops1()
except:
    print('Гавно Индекс!')

if __name__  == '__main__':
    oops1()