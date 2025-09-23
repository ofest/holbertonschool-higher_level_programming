#!/usr/bin/python3
"""Module contains class My list()"""


class MyList(list):
    """contains function print_sortmylied()"""
    def print_sorted(self):
        """Returns the sorted list and then, it print"""
        sorted(self)
        sorted_list = sorted(self)
        print(sorted_list)
