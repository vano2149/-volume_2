"""
Contains_yield.py file!! Page 146!
"""

class Iters:
    def __init__(self, value):
        self.data = value
    def __getitem__(self, i):
        print(f'get[{i}]:', end='')
    def __iter__(self):
        print(f'iter=> next:', end='')
        for x in self.data:
            yield x
            print(f'next:', end='')
    def __contains__(self, x):
        print('contains: ', end='')
        return x in self.data

if __name__ == '__main__':
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)
    for i in X:
        print(i, end=' | ')
    print()
    print([i ** 2 for i in X])
    print(list(map(bin, X)))
    I = iter(X)

    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break
