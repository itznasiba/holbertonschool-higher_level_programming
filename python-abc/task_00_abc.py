#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract Base Class representing an Animal.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        """
        pass

class Dog(Animal):
    """
    Dog class inheriting from Animal.
    """
    def sound(self):
        """
        Returns the sound of a dog.
        """
        return "Bark"

class Cat(Animal):
    """
    Cat class inheriting from Animal.
    """
    def sound(self):
        """
        Returns the sound of a cat.
        """
        return "Meow"
