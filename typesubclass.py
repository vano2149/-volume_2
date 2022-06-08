"""
File typesubclass.py
"""

class Mylist(list):
    """
    Кастомная функция списка, началом индексирования c 1!
    """
    def __getitem__(self, offset):
        print(f'indexing {self} at {offset}')
        return list.__getitem__(self, offset -1)
if __name__ == '__main__':
    print(list('abc'))
    x = Mylist('abc')
    print(x)

    print(x[1])
    print(x[3])

    x.append('spam')
    print(x)
    x.reverse()
    print(x)
