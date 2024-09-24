#!/usr/bin/python3

"""
contain the class
"""


from abc import ABC, abstractmethod


class Animal(ABC):

    """
    contain method abstract
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    """
    dog sound
    """

    def sound(self):
        return "Bark"


class Cat(Animal):

    """
    cat sound
    """

    def sound(self):
        return "Meow"
