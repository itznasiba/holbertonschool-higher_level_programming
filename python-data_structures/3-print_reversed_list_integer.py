def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers of a list in reverse order.
    One integer per line, using string formatting.
    """
    if my_list:
        # Loop through the list backwards using slicing [start:stop:step]
        for item in my_list[::-1]:
            print("{:d}".format(item))
