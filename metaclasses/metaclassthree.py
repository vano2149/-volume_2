"""
metaclassthree.py file!
"""
def MetaFunc(classname, supers, classdict):
    print('In MetaFunc: ', classname, supers, classdict)
    return type(classname, supers, classdict)

class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaFunc):
    data = 1
    def meth(self, arg):
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
