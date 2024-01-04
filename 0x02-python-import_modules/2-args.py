#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_argv = len(argv) - 1
    if num_argv < 1:
        print("{} arguments".format(num_argv))
    elif num_argv == 1:
        print("{} argument:".format(num_argv))
    else:
        print("{} arguments:".format(num_argv))
    for i in range(num_argv):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
