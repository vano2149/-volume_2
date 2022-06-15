"""
Spam_class.py file!
"""

class Spam:
    """"""
    numInstances = 0
    def __init__(self):
        """"""
        Spam.numInstances = Spam.numInstances + 1

    @staticmethod
    def printNumInstances():
        """"""
        print(f"Number of instances created: {Spam.numInstances}")

if __name__ == '__main__':
    a = Spam()
    b = Spam()
    c = Spam()
    Spam.printNumInstances()
    print('-' * 30)
    a.printNumInstances()
