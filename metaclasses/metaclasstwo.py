"""
metaclasstwo.py file!
"""

class MetaTwo(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaTwo.new: ', classname, supers, classdict)
        return type.__new__(meta, classname, supers, classdict)


    def __init__(Class, classname, supers, classdict):
        print('In MetaTwo.init: ', classname, supers, classdict)
        print('...init class object: ', list(Class.__dict__.keys()))

class Eggs:
    pass
print('making class')
class Spam(Eggs, metaclass = MetaTwo):
    data = 1
    def meth(self, arg):
        return self.data  + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
