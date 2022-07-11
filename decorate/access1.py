"""
access1.py file!
Page -> 552!
"""

traceMe = False

def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args))+ ']')

def Private(*privates):
    def onDecoratos(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.wrapped = aClass(*args, **kwargs)
            def __getattr__(self, attr):
                trace('get:', attr)
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == 'wrapped':
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)
        return onInstance
    return onDecoratos

if __name__ == '__main__':
    traceMe = True
    @Private('Data', 'size')
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start
        
        def size(self):
            return len(self.data)
        
        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        
        def display(self):
            print(f'{self.label} => {self.data}')

X = Doubler('X is', [1, 2, 3])
Y = Doubler('Y is', [-10, -20, -30])

print(Y.label)
Y.display(); Y.double()
Y.label = 'Spam'
Y.display()
