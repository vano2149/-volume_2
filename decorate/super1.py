"""
Super.py file!
Базовое исрользование встроенной функции
super и связанные с ней компромисы!!!
"""

class C:
    def act(self):
        print('spam')

class D(C):
    def act(self):
        C.act(self)
        print('eggs')

class E(C):
    def method(self):
        proxy = super()
        print(proxy)
        proxy.act()

if __name__ =='__main__':
    X = D()
    X.act()
    print("-" * 25)
    E().method()