"""
spam_class.py file!!
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

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    
    def printNumInstances(cls):
        print(f"Number of instances: {cls.numInstances}")
    
    printNumInstances = classmethod(printNumInstances)

