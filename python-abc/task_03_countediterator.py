#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)  # Create an iterator from the iterable
        self.count = 0  # Initialize the count

    def __next__(self):
        self.count += 1  # Increment the counter
        return next(self.iterator)  # Get the next item

    def get_count(self):
        return self.count  # Return the current count
