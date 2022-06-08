"""
Обобщенный инструмент тестирования!
"""
import importlib
from this import d

def tester(listerclass, sept = False):
    class Super:
        def __init__(self):
            self.data1 = 'spam'

        def ham(self):
            pass
    
    class Sub(Super, listerclass):
        def __init__(self):

            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42
        
        def spam(self):
            pass
    instance = Sub()

    print(instance)

    if sept:
        print('-' * 80)

def testByNames(modname, classname, sepr = False):
    modobject = importlib.import_module(modname)

    listerclass = getattr(modobject, classname)

    tester(listerclass, sepr)

if __name__ == '__main__':
    testByNames('listinstance', 'Listinstance', True)
