"""
"""

class Spam:
    def doit(self, message):
        print(message)


class Eggs:
    def m1(self, n):
        print(n)

    def m2(self):
        x = self.m1
        x(42)

Eggs().m2()
