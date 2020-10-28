#!/usr/bin/env python3
import sys
from os.path import exists
from typing import TextIO


def numerate_lines(source: TextIO):
    for i, line in enumerate(source):
        print("{:>6}  {}".format(i + 1, line[:-1]))


def main():
    if len(sys.argv) == 1:
        numerate_lines(sys.stdin)
    elif len(sys.argv) == 2:
        if not exists(sys.argv[1]):
            print(f"nl: {sys.argv[1]}: No such file or directory")
            return
        with open(sys.argv[1], "r") as input_file:
            numerate_lines(input_file)
    else:
        print("nl accept only 1 argument -- path to file")


if __name__ == '__main__':
    main()
