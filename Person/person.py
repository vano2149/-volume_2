"""
person.py file!
"""

class Person:
    """
    Class Person
    """
    def __init__(self, name:str, job=None, pay=0) -> None:
        self.name = name
        self.job = job
        self.pay = pay
    
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent:int)-> int:
        if percent < 0.0 or percent > 1.0:
            raise TypeError("Invalid percentage")
        self.pay = int(self.pay * (1 + percent))
    def giveRaise(self, percent:int) -> int:
        """
        Идентичный метод реализованный спомощью assert!
        """
        assert percent >= 0.0 and percent <= 1.0, "Invalid percent"
        self.pay = int(self.pay *(1 + percent))

class Manager(Person):
    """
    Настроенная версия Person co специальным требованием.
    """
    def __init__(self, name , pay):
        Person.__init__(self, name, pay)
    
    def giveRaise(self, percent, bonus=10):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    print('_' * 30)
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay = 100000)
    print(bob)
    print(sue)
    print('-' * 30)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print('-' * 30)
    print(bob.lastName(), sue.lastName())
    print('-' * 30)
    sue.giveRaise(.10)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
