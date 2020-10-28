#!/usr/bin/env python3


from typing import List


def vec_product(vec1: List[int], vec2: List[int]) -> int:
    """
    >>> vec_product([1, 2, 3], [4, 5, 6])
    32
    """
    return sum(map(lambda v1, v2: v1 * v2, vec1, vec2))


def matrix_transpose(mat: List[List]) -> List[List]:
    """
    >>> matrix_transpose([[1, 2], [3, 4], [5, 6]])
    [[1, 3, 5], [2, 4, 6]]
    """
    if len(mat) == 0:
        raise ValueError("Matrix is empty")
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]


def matrix_product(mat1: List[List[int]], mat2: List[List[int]]):
    """
    >>> mat1 = [[1, 3, 2], [0, 4, -1]]
    >>> mat2 = [[2, 0, -1, 111], [3, -2, 1, 2], [0, 1, 2, 3]]
    >>> matrix_product(mat1, mat2)
    [[11, -4, 6, 123], [12, -9, 2, 5]]
    """
    if len(mat1) == 0 or len(mat2) == 0:
        raise ValueError("One of matrix is empty")
    n, k1 = len(mat1), len(mat1[0])
    k2, m = len(mat2), len(mat2[0])
    if k1 != k2:
        raise ValueError(
            f"Can't multiply two matrices with shapes {n}x{k1} and {k2}x{m}"
        )
    mat2_t = matrix_transpose(mat2)
    return [[vec_product(vec1, vec2) for vec2 in mat2_t] for vec1 in mat1]


def matrix_pretty_print(mat: List[List[int]]):
    if len(mat) == 0:
        raise ValueError("Matrix is empty")
    n, m = len(mat), len(mat[0])
    delimiter_line = "-" * (4 * m + 1)
    row_template = "|{:>3}" * m + "|"
    for row in mat:
        print(delimiter_line)
        print(row_template.format(*row))
    print(delimiter_line)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    _mat = [[11, -4, 6, 123], [12, -9, 2, 5]]
    matrix_pretty_print(_mat)
