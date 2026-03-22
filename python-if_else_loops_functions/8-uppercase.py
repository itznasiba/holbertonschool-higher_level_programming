#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            char = chr(ord(str[i]) - 32)
        else:
            char = str[i]
        print("{}".format(char), end="")
    print("")
