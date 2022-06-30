#!/usr/bin/python3

if __name__ == '__main__':
    """"prints addition oall the arguments"""
    import sys
    
    total = 0
    for d in range(len(sys.argv) - 1):
        total += int(sys.argv[d + 1])
    print("{}".format(total))
