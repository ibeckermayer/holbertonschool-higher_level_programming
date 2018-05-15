#!/usr/bin/python3
def lookup(obj):
    """returns the list of available attributes and methods of an object

    Returns:
        list: the list of available attributes and methods of an object

    """
    return dir(obj)
