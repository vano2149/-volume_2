'''
Глава 30: Перегрузка операций, страница 124.
'''
"I am: docstr.__doc__"
def func(args):
    """I am: docstr.func.__doc__"""
    pass


class Spam:
    """I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__"""

    def method(self):
        """I am: spam.method.__doc__ of self.method.__doc__"""
        print(self.__doc__)
        print(self.method.__doc__)
