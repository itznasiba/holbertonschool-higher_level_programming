#!/usr/bin/python3

def best_score(a_dictionary):

    m = None
    ky = None
    for key, value in a_dictionary.items():
        if m == None or value > m:
            m = value
            ky = key
    return ky
