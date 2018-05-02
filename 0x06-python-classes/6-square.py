#!/usr/bin/python3
class Square:
    """a Square

    Attributes:
        size (int, optional): the size of the square
        position (tuple(int, int), optional): touple of ints
            greater than 0 to define position
    """

    def __init__(self, size=0, position=(0, 0)):
        """The constructor for square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for size

        Returns:
            int: self.__size
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position

        Args:
            position (tuple(int, int), optional): touple of ints
                greater than 0 to define position

        Raises:
            ValueError: If position is not a tuple of 2 positive integers
        """
        if not self.__is_position(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __is_position(self, value):
        """checks if a value is a valid position

        Args:
            value (tuple(int, int)): the tuple to be checked

        Returns:
            int: 1 if valid position, 0 if not
        """
        if not isinstance(value, tuple):
            return 0
        if len(value) != 2:
            return 0
        if not isinstance(value[0], int):
            return 0
        if not isinstance(value[1], int):
            return 0
        if value[0] < 0:
            return 0
        if value[1] < 0:
            return 0
        return 1

    def my_print(self):
        """Prints the square to stdout using #'s
        """
        if not self.size:
            print()
            return

        for i in range(self.position[1]):
            print()

        for i in range(self.size):
            for k in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
