#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]  # Create a shallow copy of the original list
    if idx < 0 or idx >= len(my_list):
        return new_list  # Return the copy if index is out of range
    new_list[idx] = element  # Replace the element in the copy
    return new_list  # Return the modified copy
