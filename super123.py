"""
Методы являются объектами:
связанные или несвязанные методы
"""

class Super:
    def method(self):
        pass

class Tool:
    def __method(self):
        pass    
    def other(self):
        self.__method()

class Sub1(Tool, Super):
    pass
    def actions(self):
        self.method()

class Sub2(Tool):
    def __init__(self):
        self.method = 99
