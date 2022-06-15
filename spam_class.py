"""
spam_class.py file Page 272!!
Декораторы и метаклассы
"""
'''
class Spam:
    numInstances  = 0

    def __init__(self):
        Spam.numInstances += 1

    def printNumInstances():
        print(f"Number of instances: {Spam.numInstances}")

    printNumInstances = staticmethod(printNumInstances)
'''

'''
class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    
    def printNumInstances(cls):
        print(f"Number of instances: {cls.numInstances, cls}")
    
    printNumInstances = classmethod(printNumInstances)

class Sub(Spam):
    def printNumInstances(cls):
        print("Extra stuff...", cls)
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)

class Other(Spam):
    pass
'''

class Spam:
    numInstances = 0

    def count(cls):
        cls.numInstances += 1
    
    def __init__(self):
        self.count()
    count = classmethod(count)

class Sub(Spam):
    numInstances = 0

    def __init__(self):
        Spam.__init__(self)

class Other(Spam):
    numInstances = 0

