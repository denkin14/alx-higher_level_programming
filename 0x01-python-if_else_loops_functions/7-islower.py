#!/usr/bin/python3

"""this function checks for lowercse characters"""
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
