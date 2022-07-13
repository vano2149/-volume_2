"""
access2.py file!
Page -> 559!
"""

traceMe = False

def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf:str) -> None:
    def onDecorator(aClass):
        class onInstance:
            """
            Doc String!
            """
            def __init__(self, *args, **kwargs):
                self.__wrapped = aClass(*args, **kwargs)
            
            def __getattr__(self, attr):
                trace('Get: ', attr)
                if failIf(attr):
                    raise TypeError(f'Private attribute feach: {attr}')
                
                else:
                    return getattr(self.__wrapped, attr)
            
            def __setattr__(self, attr, value):
                trace('Set: ', attr, value)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError(f"Private attribute change: {attr}")
                
                else:
                    setattr(self.__wrapped, attr, value)
        return onInstance
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))

if __name__ == '__main__':
    @Private('age')
    class Person:
        """
        Doc String a Person class!
        """
        def __init__(self, name, age):
            self.name = name
            self.age = age

    X = Person('bob smith', 40)
    print(f"Hi my name is {X.name.title()}!")
