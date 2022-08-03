"""
spam1.py file!
"""
# Page -> 604!
class Eggs: ...

class Spam(Eggs, metaclass=Meta):
    data = 1
    def meth(self, arg):
        return self.data + arg
