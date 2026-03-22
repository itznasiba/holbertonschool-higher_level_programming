#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Get the number of arguments (excluding the script name)
    n = len(sys.argv) - 1

    # Logic for the first line
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n))

    # Logic to print each argument with its index
    for i in range(1, n + 1):
        print("{}: {}".format(i, sys.argv[i]))
