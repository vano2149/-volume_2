"""
wrapp_decor.py file!
"""

def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)
        
        def __getattr__(self, name):
            return getattr(self.wrapped, name)
    
    return Wrapper

@decorator
class C:
    def __init__(self, x , y):
        self.attr = 'spam'

if __name__ == '__main__':
    x = C(6, 7)
    def __str__(self):
        return print(f'{self.x}')
