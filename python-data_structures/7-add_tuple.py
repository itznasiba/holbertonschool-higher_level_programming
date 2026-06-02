#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds 2 tuples element-wise for their first two positions.
    Missing elements default to 0, extra elements are ignored.
    """
    # Pad tuples dynamically or unpack safely by concatenating (0, 0)
    # This guarantees that at least indices 0 and 1 will always exist
    a_1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a_2 = tuple_a[1] if len(tuple_a) > 1 else 0

    b_1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b_2 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (a_1 + b_1, a_2 + b_2)
