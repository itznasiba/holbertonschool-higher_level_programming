#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    replace number
    """ 
    for i in my_list:
        if i == search:
            i = replace
    return my_list
