#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialize Square

        Args:
           size (int): size of the square
           x (int) (default 0): x position of the square
           y (int) (default 0): y position of the square
           id (int) (default None): the id of the square

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>

        Returns:
            str

        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)
