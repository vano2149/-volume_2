"""
Bothmethod_decorators.py file!
"""

class Methods:
    """"""
    def imeth(self, x):
        """"""
        print([self, x])

    @staticmethod
    def smeth(x):
        """"""
        print([x])

    @classmethod
    def cmeth(cls, x):
        """"""
        print([cls, x])

    @property
    def name(self):
        """"""
        return print('Bob ' + self.__class__.__name__)

if __name__ == '__main__':
    obj = Methods()
    obj.imeth(1)
    print('-' * 30)
    obj.smeth(2)
    print('-' * 30)
    obj.cmeth(3)
    print('-' * 30)
    obj.name
