#!/usr/bin/python3

"""
contain the class dragon vive les dragons
"""


class SwimMixin:

    """
    contain swim
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:

    """
    contain fly
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):

    """
    agrougrou
    """

    def roar(self):
        print("The dragon roars!")
