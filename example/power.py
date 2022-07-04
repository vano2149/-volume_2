"""
power.py file!
Page -> 482!
"""

class Power:
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

if __name__ == "__main__":
    X = Power(3, 4)
    print(X.square)
    print(X.cube)
    X.square = 5
    print(X.square)
