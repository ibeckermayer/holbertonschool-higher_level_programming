#!/usr/bin/python3
"""find A peak of unsorted list of integers"""


def find_peak(list_of_integers):
    """ find the peak
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1
    return(peak_helper(list_of_integers, low, high))


def peak_helper(list_of_integers, low, high):
    """help function for find_peak
    """
    if low == high:
        return(list_of_integers[high])

    mid = (high + low) // 2

    if list_of_integers[mid] > list_of_integers[mid + 1]:
        return(peak_helper(list_of_integers, low, mid))
    return(peak_helper(list_of_integers, mid + 1, high))
