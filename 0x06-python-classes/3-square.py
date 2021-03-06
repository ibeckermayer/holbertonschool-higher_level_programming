#!/usr/bin/python3
class Square:
    """a Square"""

    def __init__(self, size=0):
        """The constructor for square

        Args:
            size (int): Size of the square

        Raises:
            AttributeError: If size isn't an integer
            ValueError: If size < 0

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if not size >= 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the current square area

        Returns:
            int: the square of the size
        """
        return self.__size**2
