"""
"""
class ListInherited:
    """
    Применяет dir() для сбора отрибутов экземпляра.
    """
    def __attrnames(self, indent=' ' * 4):
        result = f"Unders{'-' * 77}\n{indent}\nOthers{'-' * 77}"
        unders = []
        for attr in dir(self):
            if attr[:2] == "__" and attr[-2:] == '__':
                unders.append(attr)
            else:
                display = str(getattr(self, attr))[:82 -(len(indent) + len(attr))]
                result += f'{indent}={attr}{display}\n'
        return result 
    
    def __str__(self):
        return  '<Instance of %s, address %s:\n%s>' % (self.__class__.__name__, id(self), self.__attrnames())

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)