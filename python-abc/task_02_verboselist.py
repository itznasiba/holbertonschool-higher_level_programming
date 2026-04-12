#!/usr/bin/env python3
"""
This module defines the VerboseList class that extends the built-in list.
"""


class VerboseList(list):
    """
    A list subclass that prints notifications when items are added or removed.
    """

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extends the list and prints a notification with the count."""
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Prints a notification before removing an item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Prints a notification before popping an item."""
        # Get the item that will be popped to include it in the message
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
