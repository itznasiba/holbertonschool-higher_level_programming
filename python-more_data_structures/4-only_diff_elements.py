#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set = []
    set_u = []
     for i in set_1:
         for j in set_2:
             if i == j:
                 new_set.append(i)
    for i in set_1:
        if i in new_set:
            continue
        else:
            set_u.append(i)
    for j in set_2:
        if j in new_set:
            continue
        else:
            set_u.append(j)
    return set_u
