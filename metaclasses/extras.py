"""
extras.py file!
"""

class Extras:
    def extra(self, args):
        ...

class Client1(Extras): ...
class Client2(Extras): ...
class Client3(Extras): ...

X = Client1()
X.extra()
