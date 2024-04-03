#!/usr/bin/python3
"""Square Class Documentation"""


class Square:
    """Define class attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor:

        Args:
            size (int): length of square side
            position (int, int): coordinates of square
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """Get/set the position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Area of square

        Returns:
            size squared
        """
        return self.__size ** 2

    @property
    def size(self):
        """get/set the size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
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
        for i in range(self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
        print("")
