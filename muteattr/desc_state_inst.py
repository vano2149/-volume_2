"""
desc_state_inst.py file!
Page -> 470!
"""

from ast import In


class InstState:
    def __get__(self, instance, owner):
        print('InstState get...')
        return instance._X * 10
    
    def __set__(self, instance, value):
        print('InstState set...')
        instance._X = value
    
class CalcAttrs:
    X = InstState()
    Y = 3
    def __init__(self):
        self._X = 2
        self.Z = 4
obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)
obj.X = 5
CalcAttrs.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)

obj2 = CalcAttrs()
print(obj2.X, obj2.Y, obj2.Z)