#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class
    """

    def __init__(self, size):
        """initializes Square

        Attributes:
            self.__size: size of one side of the square

        Args:
            size: size of one side of the square

        """
        super().__init__(size, size)
        super().integer_validator("size", size)

        self.__size = size
