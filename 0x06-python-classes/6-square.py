#!/usr/bin/python3
"""Square Class Documentation"""


class Square:
    """Define class attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor:

        Args:
            size: length of square side
            position: coordinates of square

        Raises:
            TypeError: if size is not an int
            ValueError: if size is a negative number
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """Get/set the position"""
        return self.__position

    @position.setter
    def position(self, val):
        if (not isinstance(val, tuple) or
                len(val) != 2 or
                not all(isinstance(num, int) for num in val) or
                not all(num >= 0 for num in val)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = val

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
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.position[1])]
        for i in range(self.size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
        print("")
