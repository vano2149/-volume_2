"""
spam1.py file!
Конец! / End!
"""
# Page -> 604!
class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict)
        return type.__new__(meta, classname, supers, classdict)

class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaOne):
    data = 1
    def meth(self, arg):
        return self.data + arg

print('meking instance')
X = Spam()
print('data:', X.data, X.meth(2))
