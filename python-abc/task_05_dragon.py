#!/usr/bin/env python3
"""
This module demonstrates Mixins by creating a Dragon class
that can both swim and fly.
"""


class SwimMixin:
    """Mixin to add swimming capability."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin to add flying capability."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits from both SwimMixin and FlyMixin.
    It can swim, fly, and roar.
    """
    def roar(self):
        print("The dragon roars!")
