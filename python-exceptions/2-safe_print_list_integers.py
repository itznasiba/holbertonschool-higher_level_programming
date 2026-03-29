#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range (x):
        try:
            n = n + 1
            print("{:d}".format(my_list[i]))
        except IndexError:
            return n
        except (ValueError, TypeError):
            continue
