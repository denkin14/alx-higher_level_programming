#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dir = a_dictionary.copy()
    list_keys = list(my_dir.keys())

    for i in list_keys:
        my_dir[1] *= 2
    return (my_dir)
