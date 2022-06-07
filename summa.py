"""
Page 190!
"""

def square(arg):
    return arg ** 2

class Sum:
    def __init__(self, val):
        self.val = val
    
    def __call__(self, arg):
        return self.val + arg
    
class Product:
    def __init__(self, val):
        self.val = val

    def method(self, arg):
        return self.val * arg

class Negate:
    def __init__(self, val):
        self.val = -val

    def __repr__(self):
        return str(self.val)

if __name__ == '__main__':
    subject = Sum(2)
    pobject = Product(3)
    actions = [square, subject, pobject.method, Negate]
    for act in actions:
        print(act(5))


    print('-' * 15)
    print(actions[-1](5))
    print('-'*15)
    print([act(5) for act in actions])
    print('-'*15)
    print(list(map(lambda act: act(5), actions)))
    print('-' * 15)
    print([act(5) for act in actions])
    table = {act(5): act for act in actions}
    for key, value in table.items():
        print('{0:2} => {1}'.format(key, value))
    print('-'* 15)
    