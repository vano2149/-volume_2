"""
"""

from employees import PizzaRobot, Server


class Customer:
    """
    """
    def __init__(self, name):
        """
        """
        self.name = name

    def order(self, server):
        """
        """
        print(f"{self.name} orders form {server}")

    def pay(self, server):
        """
        """
        print(f"{self.name} pays for item to {server}")

class Oven:
    def bake(self):
        """
        """
        print("oven bakes")

class PizzaShop:
    """
    """
    def __init__(self):
        """
        """
        self.server = Server("Pat")
        self.chef = PizzaRobot("Bob")
        self.oven = Oven()

    def order(self, name):
        """
        """
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == '__main__':

    print('-' * 26)
    scene = PizzaShop()
    scene.order('Homer')
    print('-' * 26)
    print('...')
    scene.order('Shaggy')
    print('-' * 26)