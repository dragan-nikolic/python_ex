"""
Pylint Tutorial
"""

#pylint: disable=too-few-public-methods

class Car:
    """class docstring"""
    def __init__(self, color):
        self.color = color


my_car = Car('blue')

def crash(car1, car2): #pylint: disable=unused-argument
    """function docstring"""
    car1.color = 'burnt'

crash(Car('red'), my_car)
