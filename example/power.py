"""
power.py file!
Page -> 482!
"""
'''
class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
    def getSquare(self):
        return self._square ** 2
    def setSquare(self, value):
        self._square = value
    square = property(getSquare, setSquare)

    def getCube(self):
        return self._cube ** 3
    cube = property(getCube)
'''

'''
class DescSquare:
    def __get__(self, instance, owner):
        return instance._square ** 2
    def __set__(self, instance, value):
        instance._square = value
class DescCube:
    def __get__(self, instance, owner):
        return instance._cube ** 3

class Powers:
    square = DescSquare()
    cube = DescCube()
    
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
'''

class Powers:
    
    def __init__(self, square, cube):
        self._square = square
        self._cobe = cube
    
    def __getattr__(self, name):
        if name == 'square':
            return self._square ** 2
        elif name == 'cube':
            return self._cobe ** 3
        else:
            raise TypeError(f'Unknow attr: {name}')
    
    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value
        else:self.__dict__[name] = value


if __name__ == "__main__":
    X = Powers(3, 4)
    print(X.square)
    print(X.cube)
    X.square = 5
    print(X.square)
