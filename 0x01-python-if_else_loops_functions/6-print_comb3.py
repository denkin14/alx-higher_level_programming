#!/usr/bin/python3

for my_digit1 in range(0, 10):
    for my_digit2 in range(my_digit1 + 1, 10):
        if my_digit1 == 8 and my_digit2 == 9:
            print("{}{}".format(my_digit1, my_digit2))
        else:
            print("{}{}".format(my_digit1, my_digit2), end=", ")
