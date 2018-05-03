#!/usr/bin/python3
def print_square(size):
    """prints a square with #

    Args:
       size (int): size of the square

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        ValueError: size must be >=0
        TypeError: size must be an int

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if not size >= 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
