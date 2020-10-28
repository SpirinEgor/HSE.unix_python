#!/usr/bin/env python3
import sys
from os.path import exists
from typing import TextIO


def tail(source: TextIO, tail_size: int = 10):
    lines_queue = []
    for line in source:
        if len(lines_queue) == tail_size:
            lines_queue.pop(0)
        lines_queue.append(line[:-1])
    print('\n'.join(lines_queue))


def main():
    if len(sys.argv) == 1:
        tail(sys.stdin)
        return
    for i, filepath in enumerate(sys.argv[1:]):
        if not exists(filepath):
            print(f"tail: {filepath}: No such file or directory")
            continue
        print(f"==> {filepath} <==")
        with open(filepath, "r") as input_file:
            tail(input_file)
        if i != len(sys.argv) - 2:
            print()


if __name__ == '__main__':
    main()
