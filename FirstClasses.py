"""
"""
# Подсчет элементов с помощью Counter
#from collections import Counter
#count = list('missisipi')
#print(Counter(count))


class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


class SecondClass(FirstClass):
    def display(self):
        print(f'Current value = {self.data}')


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return f"ThirdClass: {self.data}"

    def mul(self, other):
        self.data *= other

a = ThirdClass('abc')
a.display()
print(a)

b = a + 'xyz'
b.display()
print(b)

a.mul(3)
print(a)
