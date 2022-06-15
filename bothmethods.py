"""
File bothmethods.py page 266!
"""

class Methods:
    def imeth(self, x):
        print([self, x])
    
    def smeth(x):
        print([x])
    
    def cmeth(cls, x):
        print([cls, x])

@staticmethod(smeth)

@classmethod(cmeth)