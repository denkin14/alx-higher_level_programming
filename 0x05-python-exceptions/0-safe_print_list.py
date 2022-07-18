#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints x elements of list

    my_list(list): the list to print elements from
    x (int): the number of elements of my_list to print.

    returns: the number of elements printed
    """
    dmk = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            dmk += 1
        except IndexError:
            break
        print("")
        return(dmk)
