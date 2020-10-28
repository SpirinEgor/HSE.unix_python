#!/usr/bin/env python3
import sys
from os.path import exists
from typing import TextIO, Tuple


def word_count(source: TextIO) -> Tuple[int, int, int]:
    n_newlines = n_words = n_bytes = 0
    for line in source:
        n_newlines += 1
        n_words += len(line.split())
        n_bytes += len(line.encode())
    return n_newlines, n_words, n_bytes


def print_wc_style(
        n_newlines: int, n_words: int, n_bytes: int, name: str = None
):
    stats = "{:>8}{:>8}{:>8}".format(n_newlines, n_words, n_bytes)
    if name is None:
        print(stats)
    else:
        print(f"{stats} {name}")


def main():
    if len(sys.argv) == 1:
        print_wc_style(*word_count(sys.stdin))
        return
    total_newlines = total_words = total_bytes = 0
    for filepath in sys.argv[1:]:
        if not exists(filepath):
            print(f"wc: {filepath}: No such file or directory")
            continue
        with open(filepath, "r") as input_file:
            n_newlines, n_words, n_bytes = word_count(input_file)
        print_wc_style(n_newlines, n_words, n_bytes, filepath)
        total_newlines += n_newlines
        total_words += n_words
        total_bytes += n_bytes
    if len(sys.argv) > 2:
        print_wc_style(total_newlines, total_words, total_bytes, "Total")


if __name__ == '__main__':
    main()
