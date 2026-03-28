#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    m = None
    ky = None
    for key, value in a_dictionary.items():
        if m is None or value > m:
            m = value
            ky = key
    return ky
