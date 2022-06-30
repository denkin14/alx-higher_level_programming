#!/usr/bin/python3

if __name__ == '__main__':
    """"print number and list arguments"""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for d in range(count):
        print("{}: {}".format(d + 1, sys.argv[d + 1]))
