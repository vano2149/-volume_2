"""
person.py file!
"""

class Person:
    """
    Класс Person ПРИМЕР docstr!
    """
    def __init__(self, name):
        self._name = name

    def __getattr__(self, attr):
        print(f'Get: ' + attr)
        if attr == 'name':
            return self._name
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        print(f"Set: " + attr)
        if attr == 'name':
            attr = '_name'
        self.__dict__[attr] = value

    def __delattr__(self, attr):
        print('Del:' + attr)
        if attr == 'name':
            attr = '_name'
        del self.__dict__[attr]


if __name__ == '__main__':
    bob = Person('Bob Smith')
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)
    del bob.name
    print('-' * 20)
    sue = Person('Sue Jones')
    print(sue.name)
