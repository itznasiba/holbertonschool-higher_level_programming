#!/usr/bin/env python3
"""
This module defines the CountedIterator class.
"""


class CountedIterator:
    """
    An iterator wrapper that keeps track of the number of items iterated.
    """

    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable object.

        Args:
            iterable: Any object that can be converted into an iterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Returns the current number of items that have been iterated.
        """
        return self.count

    def __next__(self):
        """
        Fetches the next item from the iterator and increments the counter.

        Raises:
            StopIteration: If there are no more items to iterate.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Returns the iterator object itself.
        Required for an object to be considered an 'iterator'.
        """
        return self
