#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


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

    def area(self):
        return self.radius**2 * math.pi

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(obj):
    obj_area = obj.area()
    obj_perimeter = obj.perimeter()
    print(f"Area: {obj_area}")
    print(f"Perimeter: {obj_perimeter}")
