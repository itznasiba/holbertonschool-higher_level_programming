#!/usr/bin/env python3
"""
This module demonstrates multiple inheritance with Fish, Bird, and FlyingFish.
"""


class Fish:
    """Class representing a Fish."""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Class representing a Bird."""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish inherits from both Fish and Bird.
    Because Fish is listed first, Python looks there first for methods.
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
