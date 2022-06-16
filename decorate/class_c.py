"""
class_c.py file!
Страница 294! Связанность: 
Приложение для подмешиваемых классов!
"""

"""
class A:
    def __init__(self):
        print('A.__init__')

class B(A):
    def __init__(self):
        print('B.__init__')
        A.__init__(self)

class C(A):
    def __init__(self):
        print('C.__init__')
        A.__init__(self)

class D(B, A):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
"""

class A:
    def __init__(self): print('A.__init__')

class B(A):
    def __init__(self): print("B.__init__"); super().__init__()

class C(A):
    def __init__(self): print('C.__init__'); super().__init__()

class D(B, C):
    pass


if __name__ == '__main__':
    x = B()
    print(f"Обращение к B: {x}")
    print('-'* 25)
    c = C()
    print(f"Обращение к С: {c}")
    print('-'* 25)
    x = D()
    print(f'Обращение к D: {x}')
    print(B.__mro__)
    print(D.__mro__)