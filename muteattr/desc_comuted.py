"""
desc_computed.py file!
Page -> 496!
"""

class Descriptor:
    def __init__(self, start):
        self.value = start
    
    def __get__(self, instance, owner):
        return self.value ** 2
    
    def __set__(self, instance, value):
        self.value = value

class Client1:
    X = Descriptor(3)

class Client2:
    X = Descriptor(32)

c1 = Client1()
c2 = Client2()

print(c1.X)
c1.X = 4
print(c1.X)
print(c2.X)
