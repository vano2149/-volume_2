"""
validate_descriptor1.py file!
Page -> 496!
"""

class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

class Name:
    def __get__(self, instance, owner):
        return self.name
    
    def __set__(self, instance, value):
        value = value.lower().replace(' ', '_')
        self.name = value
    
name = Name()

class Age:
    def __get__(self, instance, owner):
        return self.age
    def __set__(self, instance, value):
        if value < 0 or value > 150:
            raise ValueError("Invalid Age!")
        else:
            self.age = value

age = Age()

class Acct:
    def __get__(self, instance, owner):
        return self.acct[:-3] + "***"

    def __set__(self, instance, value):
        value = value.replace('-', '')
        if len(value) != instance.acctlen:
            raise TypeError("Invalid acct number!")
        else:
            self.acct = value
acct = Acct()

class Remain:
    def __get__(self, instance, owner):
        return instance.retireage - instance.age
    def __set__(self, instance, value):
        raise TypeError('Cannot set remain')

remain = Remain()
