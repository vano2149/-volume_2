"""
"""

class C1:

    def math1(self):
        self.__X = 88

    def math2(self):

        print(self.__X)

class C2:

    def metha(self):
        self.__X = 99

    def methb(self):
        print(self.__X)

class C3(C1, C2):
    pass

I = C3()
I.math1()
I.metha()
print(I.__dict__)
I.math2()
I.methb()