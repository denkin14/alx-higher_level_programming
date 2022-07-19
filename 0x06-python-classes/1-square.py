#!/usr/bin/python3
""" class square that defines a square by:
    (based on file 0-square.py)
    """

class Square:
    """Square class with private attribute -
    size
    """

    def __init__(self, size):
        """initializes the size variable as
        private instance attribute
        """
        self.__size = size
