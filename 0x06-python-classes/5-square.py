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

    def area(self):
        """Area of square

        Returns:
            size squared
        """
        return self.__size ** 2

    @property
    def size(self):
        """Size of square

        Returns: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of square size

        Returns:
            none
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """Prints the square"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
