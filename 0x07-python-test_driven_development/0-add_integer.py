#!/usr/bin/python3
def add_integer(a, b=98):
    """adds two integers together

    Args:
       a (int): first integer
       b (int) (default 98): second integer

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b aren't integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
