#!/usr/bin/python3

from abc import ABC

class Animal:

    @abstractmethod
    def sound(self):

class Dog(Animal):

    super.sound(Animal, Dog)
        return "Bark"

class Cat(Animal):

    super.sound(Cat)
        return "Meow"
