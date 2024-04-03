#!/usr/bin/python3
"""Square Class Documentation"""


class Square:
    """Define class attributes"""

    def __init__(self, size=0):
        """Constructor:

        Args:
            size: length of square side

        Raises:
            TypeError: if size is not an int
            ValueError: if size is a negative number
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
