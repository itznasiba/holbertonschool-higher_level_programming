#!/usr/bin/python3
"""
module defines mylist
"""

class MyList(list):
    """
    public class MyList
    """

    def print_sorted(self):
        """
        prints sorted list
        """
        print(sorted(self))
