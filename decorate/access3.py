"""
access3.py file!
"""

def accessControl(foilIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.__wrapped = aClass(*args, **kwargs)
            def __str__(self):
                return str(self.__wrapped)
            def __add__(self, other):
                return self.__wrapped + other
            def __getitem__(self, index):
                return self.__wrapped[index]
            def __call__(self, *args, **kwargs):
                return self.__wrapped(*args, **kwargs)

        return onInstance
    return onDecorator

