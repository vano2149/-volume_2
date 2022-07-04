"""
catcher.py file!
"""

class Catcher:
    """
    """
    def __getattribute__(self, name):
        print(f'Get: {name}')
    def __setattr__(self, name, value):
        print(f'Set: {name , value}')

if __name__ == '__main__':
    X = Catcher()
    X.job
    X.pay
    X.pay = 99
