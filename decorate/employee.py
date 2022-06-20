"""
Page -> 302!
Изменение атрибутов классов
может именть побочный эффект!
"""


class Employee:
    """"""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Chef1(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

class Server1(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

class Chef2(Employee):
    def __init__(self, name):
        super().__init__(name, 50000)

class Server2(Employee):
    def __init__(self, name):
        super().__init__(name, 40000)

class TwoJobs(Chef1, Server1):
    def __init__(self, name):
        Employee.__init__(self, name, 70000)


if __name__ == '__main__':
    bob = Chef1('Bob')
    sue = Server1('Sue')
    print(bob.salary, sue.salary)
    print('-'*20)
    bob = Chef2('Bob')
    sue = Server2("Sue")
    print(bob.salary, sue.salary)
    print('Ниже ошибка!')
    tom = TwoJobs('Tom')
    print(tom.salary)

