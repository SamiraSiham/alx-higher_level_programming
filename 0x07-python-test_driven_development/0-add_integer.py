#!/usr/bin/python3
def add_integer(a, b=98):
    """Add two int numbers.
    Args:
        a: first number.
        b: second number.
    
    Raises:
        TypeError: if a or b are not int or float.
    
    Returns:
        the sum of a and b.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
