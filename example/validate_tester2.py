"""
validate_tester2.py file!
Page -> 497!
"""
from validate_tester import loadclass
CardHolder = loadclass()

bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
print('bob: ', bob.name, bob.acct, bob.age, bob.addr)

sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124, main st')
print('sue: ', sue.name, sue.acct, sue.age, sue.addr)

print('bob: ', bob.name, bob.acct, bob.age, bob.addr)

