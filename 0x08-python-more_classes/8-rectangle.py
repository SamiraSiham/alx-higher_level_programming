#!/usr/bin/python3

"""Rectangle class Documentation"""


class Rectangle:
    """Rectangle class attributes"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor.
        Args:
            width: width of rectangle
            height: height of rectangle
        Raises:
            TypeError: if width or height are not int
            ValueError: if width or height are negative numbers
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Calculate the area of rectangle
        Returns: the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle
        Returns: the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print the rectangle"""
        rect = ""
        if self.__width != 0 and self.__height != 0:
            rect += "\n".join(str(self.print_symbol) * self.__width
                              for j in range(self.__height))
        return rect

    def __repr__(self):
        """returns a string representation of the object for reproduction"""
        return "Rectangle(" + str(self._width) + ", " + str(self.__height) + ")"

    def __del__(self):
        """print a message when an object is destroyed"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns the bigger of two rectangles
        Args:
            rect_1: 1st rectangle
            rect_2: 2nd rectangle
        Raises:
            TypeError: if one of the args is not a rectangle
        Returns:
            the rectangle with the larger area
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle"i)
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
