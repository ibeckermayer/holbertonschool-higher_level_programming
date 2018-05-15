#!/usr/bin/python3

def is_same_class(obj, a_class):
    """checks if an object is exactly an instance of the specified class

    Args:
       obj (class): the object to be checked
       a_class (object): the class you're looking for

    Returns:
        bool: True if an instance, otherwise False

    """
    return type(obj) == a_class
