#/usr/bin/python3
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self, radius):
        return self.radius * 3.14

    def perimeter(self, radius):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self, width, height):
        return self.height * self.width

    def perimeter(self, radius):
        return 2 * (self.width + self.height)

def shape_info(self):
    