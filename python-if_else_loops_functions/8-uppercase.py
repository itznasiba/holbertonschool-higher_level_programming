#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if str[i] >= 'A' and str[i] <= 'Z':
            continue
        elif str[i] >= 'a' and str[i] <= 'z':
            str[i] = chr(ord(str[i]) + 32)
