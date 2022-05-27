"""
Страница 82
"""

class Person:
    """
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return f"<Person:{self.name}, {self.pay}>"


class Manager(Person):
    """
    """
    def __init__(self,name, pay):
        self.person = Person(name, 'mgr', pay)
    
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __repr__(self):
        return str(self.person)

class Departament:
    def __init__(self, *args):
        
        self.members = list(args)
    
    def addMember(self,person):
        self.members.append(person)
    
    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    
    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    print('-' * 26)
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Smith', 50000)
    

    development = Departament(bob, sue)
    development.addMember(tom)
    development.giveRaise(.10)
    development.showAll()
    print('-' * 26)

