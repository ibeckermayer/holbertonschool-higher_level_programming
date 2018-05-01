#!/usr/bin/python3
class Square:
    """a Square with private size attribute"""

    def __init__(self, size):
        """The constructor for square

        Args:
            size (int): Size of the square
        """
        self.__size = size
