#!/usr/bin/python3

def print_last_digit(number):
    if number >= 0:
        print(number % 10)
        return (number % 10)
    else:
        print((abs(number) % 10)*(-1))
        return ((abs(number) % 10)*(-1))
