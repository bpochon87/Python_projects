# Contain at least one abstract method.
# Contain at least one regular method.
# Create child class that defines implementation of its parents abstract method.
# Create an object that utilizes both parent and child methods.

""" A good way to think of abstraction is the Parent class saying 'if you're going to
    inherit from me then you need to override this abstract method(s) of mine and if you
    don't I will not let you be instantiated'.
"""
# This is a decorator: the @abstractmethod
from abc import ABC, abstractmethod

# Parent class.
class Vehicle(ABC):
    def vehicleModel(self, model):
        print("This vehicle's model is a {}.".format(model))

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def buy(self):
        pass

# Child class.
class Van(Vehicle):
    def go(self, manufacturer):
        print("You drove a {} van.".format(manufacturer))

    def buy(self, manufacturer):
        print("Would you like to buy the {} van?".format(manufacturer))

obj = Van()
obj.vehicleModel("NV3500")
obj.go("Nissan")
obj.buy("Nissan")
