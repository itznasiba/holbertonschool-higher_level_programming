#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if str[i] >= 'A' and str[i] <= 'Z':
            char = str[i]
        elif str[i] >= 'a' and str[i] <= 'z':
            char = chr(ord(str[i]) - 32)
    print("{}".format(char), end="")
    print(" ")
