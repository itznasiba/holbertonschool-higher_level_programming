#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if str[i] >= 'A' and str[i] <= 'Z':
            print("{}".format(str[i]))
        elif str[i] >= 'a' and str[i] <= 'z':
            print("{}".format(chr(ord(str[i]) - 32)))
