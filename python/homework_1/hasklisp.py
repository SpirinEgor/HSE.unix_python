#!/usr/bin/env python3

import typing as tp

from collections import namedtuple

Nil = namedtuple('Nil', ())
Cons = namedtuple('Cons', ('car', 'cdr'))
List = tp.Union[Nil, Cons]


def null(lst: List) -> bool:
    """
    >>> null(Nil())
    True
    >>> null(Cons(0, Nil()))
    False
    """
    return isinstance(lst, Nil)


def from_seq(seq: tp.Sequence) -> List:
    """
    >>> from_seq([])
    Nil()
    >>> from_seq(tuple())
    Nil()
    >>> from_seq([1, 2, 3])
    Cons(car=1, cdr=Cons(car=2, cdr=Cons(car=3, cdr=Nil())))
    """
    return Nil() if len(seq) == 0 else Cons(car=seq[0], cdr=from_seq(seq[1:]))


def head(lst: List):
    """
    >>> head(from_seq([1, 2, 3]))
    1
    >>> head(Nil())
    Traceback (most recent call last):
    ...
    AttributeError: 'Nil' object has no attribute 'car'
    """
    return lst.car


def tail(lst: List) -> List:
    """
    >>> tail(from_seq([1, 2, 3]))
    Cons(car=2, cdr=Cons(car=3, cdr=Nil()))
    >>> tail(from_seq([]))
    Traceback (most recent call last):
    ...
    AttributeError: 'Nil' object has no attribute 'cdr'
    """
    return lst.cdr


def foldr(func: tp.Callable, acc, lst: List):
    """
    >>> foldr(lambda x, y: x + y, 0, Nil())
    0
    >>> foldr(lambda x, y: x + y, 2, from_seq([1, 2, 3]))
    8
    >>> foldr(lambda x, y: x - y, 1, from_seq([3, 2, 1]))
    1
    """
    return acc if null(lst) else func(head(lst), foldr(func, acc, tail(lst)))


def foldl(func: tp.Callable, acc, lst: List):
    """
    >>> foldl(lambda x, y: x + y, 0, Nil())
    0
    >>> foldl(lambda x, y: x + y, 2, from_seq([1, 2, 3]))
    8
    >>> foldl(lambda x, y: x - y, 1, from_seq([3, 2, 1]))
    -5
    """
    return acc if null(lst) else foldl(func, func(acc, head(lst)), tail(lst))


def length(lst: List) -> int:
    """
    >>> length(Nil())
    0
    >>> length(from_seq((1, 2)))
    2
    """
    return 0 if null(lst) else 1 + length(tail(lst))


def to_list(lst: List) -> tp.List:
    """
    >>> to_list(Nil())
    []
    >>> to_list(Cons(1, Nil()))
    [1]
    >>> to_list(from_seq([1, 2, 3]))
    [1, 2, 3]
    """
    return [] if null(lst) else [head(lst)] + to_list(tail(lst))


def map_(func: tp.Callable, lst: List) -> List:
    """
    >>> to_list(map_(lambda x: x, Nil()))
    []
    >>> to_list(map_(lambda x: x, from_seq([1, 2, 3])))
    [1, 2, 3]
    >>> to_list(map_(lambda x: str(x) + '0', from_seq([1, 2, 3])))
    ['10', '20', '30']
    """
    return Nil() if null(lst) else Cons(
        car=func(head(lst)), cdr=map_(func, tail(lst))
    )


def append(lst1: List, lst2: List):
    """
    >>> append(Nil(), from_seq([]))
    Nil()
    >>> append(Nil(), Cons(0, Cons(1, Nil())))
    Cons(car=0, cdr=Cons(car=1, cdr=Nil()))
    >>> append(from_seq([1]), Nil())
    Cons(car=1, cdr=Nil())
    >>> append(from_seq([1, 2]), from_seq([3]))
    Cons(car=1, cdr=Cons(car=2, cdr=Cons(car=3, cdr=Nil())))
    """
    return lst2 if null(lst1) else Cons(
        car=head(lst1), cdr=append(tail(lst1), lst2)
    )


def filter_(pred: tp.Callable, lst: List) -> List:
    """
    >>> filter_(lambda x: True, Nil())
    Nil()
    >>> to_list(filter_(lambda x: True, from_seq([1, 2])))
    [1, 2]
    >>> to_list(filter_(lambda x: False, from_seq([1, 2])))
    []
    >>> to_list(filter_(lambda x: x % 2 == 0, from_seq(range(5))))
    [0, 2, 4]
    """
    return Nil() if null(lst) else (
        Cons(car=head(lst), cdr=filter_(pred, tail(lst)))
        if pred(head(lst)) else
        filter_(pred, tail(lst))
    )


def reverse(lst: List) -> List:
    """
    >>> reverse(Nil())
    Nil()
    >>> to_list(reverse(from_seq(range(2))))
    [1, 0]
    >>> to_list(reverse(from_seq(range(3))))
    [2, 1, 0]
    """
    if null(lst) or null(tail(lst)):
        return lst
    reversed_tail = reverse(tail(lst))
    return Cons(
        car=head(reversed_tail),
        cdr=append(tail(reversed_tail), Cons(car=head(lst), cdr=Nil()))
    )


def elem(value, lst: List) -> bool:
    """
    >>> elem(10, Nil())
    False
    >>> elem(5, from_seq(range(5)))
    False
    >>> elem(5, from_seq(range(10)))
    True
    """
    return not null(lst) and (head(lst) == value or elem(value, tail(lst)))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
