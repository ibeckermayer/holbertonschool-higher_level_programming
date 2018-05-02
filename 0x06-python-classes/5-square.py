#!/usr/bin/python3
class Square:
    """a Square

    Attributes:
        size (int): the size of the square
    """

    def __init__(self, size=0):
        """The constructor for square

        Args:
            size (int, optional): Size of the square
        """
        self.size = size

    def area(self):
        """Returns the current square area

        Returns:
            int: the square of the size
        """
        return self.size**2

    @property
    def size(self):
        """Getter for size

        Returns:
            int: self.__size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size

        Args:
            value (int, optional): Size of the square

        Raises:
            AttributeError: If value isn't an integer
            ValueError: If value < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if not value >= 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """Prints the square to stdout using #'s
        """
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
        if not self.size:
            print()
