"""
Cтраница 133!.
"""

class Super:
    def method(self):
        print('in Supper.method')
    def delegate(self):
        self.action()

class Inheritar(Super):
    pass

class Replacer(Super):
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):
    def action(self):
        print('in Provider.action')

if __name__ == '__main__':
    for klass in (Inheritar, Replacer, Provider):
        print('\n' + klass.__name__ + '...')
        klass().method()
    
    print('\nProvider...')
    x = Provider()
    x.delegate()