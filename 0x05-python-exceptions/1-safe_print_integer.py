#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with "{:d}".format().
    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
    except:
        return False
    return True
