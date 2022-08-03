"""
metaclass.pt file!
Page -> 614!
"""

class MetaObj:
    def __call__(self, classname, supers, classdict):
        print ('In MetaObj.call: ', classname, supers, classdict)
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname,supers, classdict)
        return Class
    
    def __New__(self, classname, supers, classdict):
        print('In MetaObj.new: ', classname, supers, classdict)
        return type(classname, supers, classdict)
    
    def __Init__(self, Class, classname, supers, classdict):
        print('In MetaObj.init: ', classname, supers, classdict)
        print('...init class object: ', list(Class.__dict__.keys()))

class Eggs:
    pass
print('making class')
class Spam(Eggs, metaclass=MetaObj()):
    data = 1
    def meth(self, arg):
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
