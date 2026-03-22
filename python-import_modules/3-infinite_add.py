#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    # Iterate through all arguments except the script name
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
print("{}".format(total))
