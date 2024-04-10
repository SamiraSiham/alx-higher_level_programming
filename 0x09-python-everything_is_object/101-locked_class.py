#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """
    Prevent users from creating new instance attributes
    unless the instance attribute is called 'first_name'
    """

    __slots__ = ["first_name"]
