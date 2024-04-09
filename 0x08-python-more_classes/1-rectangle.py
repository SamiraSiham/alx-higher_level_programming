#!/usr/bin/python3

"""Rectangle class Documentation"""


class Rectangle:
    """Rectangle class attributes"""
    def __init__(self, width=0, height=0):
        """Constructor.
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Width of Rectangle

        Returns: width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the value of rectangle width
        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Height of Rectangle
        Returns: the value of the rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the value of rectangle height
        Returns: none
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
