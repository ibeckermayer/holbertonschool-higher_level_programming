#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """checks if an obj is an instance of the specified class or an instance of
    a class that inherited from a_class

    Args:
       obj (class): the object to be checked
       a_class (object): the class you're looking for

    Returns:
        bool: True if an instance, otherwise False

    """
    return isinstance(obj, a_class)
