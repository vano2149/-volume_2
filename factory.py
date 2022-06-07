"""
Cтр. Множественное наследование:
'Подмешивание' классы!
"""

def factory(aClass, *args, **kwargs):
    return aClass(*args, **kwargs)

class Spam:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job

object1= factory(Spam)
object2 = factory(Person, "Arthur", 'King')
object3 = factory(Person, name='Brian')
