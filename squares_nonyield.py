"""
Page 143!
"""

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        """"""
        return SquaresIter(self.start, self.stop)
        
class SquaresIter:
    ''''''
    def __init__(self, start, stop):
        ''''''
        self.value = start - 1
        self.stop = stop
    def __next__(self):
        ''''''
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
