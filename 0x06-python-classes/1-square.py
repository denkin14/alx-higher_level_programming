#!/usr/bin/python3
"""class Square that defines a square by: 
(based on 0-square.py)
"""


class Square:
    """Square class with  private attribute -
    size.
    """

    def __init__(self, size):
        """Initializes the size variable as a private
        instance artribute
        """
        self.__size = size
