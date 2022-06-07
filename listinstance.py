"""
"""

class Listinstance:
    """
    Подмешиваемый класс!
    """
    def __attrname(self):
        result=''
        for attr in sorted(self.__dict__):
            result += f'\t{attr}={self.__dict__[attr]}'
        return result
    def __str__(self):
        return f'<Instance of {self.__class__.__name__}, address :{id(self)}\n{self.__attrname}>'

if __name__ == '__main__':
    import testmixin
    testmixin.tester(Listinstance)