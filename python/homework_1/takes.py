#!/usr/bin/env python3
from typing import Callable


def takes(*types) -> Callable:
    def type_check_decorator(function: Callable) -> Callable:
        def wrapper(*args):
            for check_type, arg in zip(types, args):
                if not isinstance(arg, check_type):
                    raise TypeError(f"Expected type {arg} to be {check_type}")
            return function(*args)
        return wrapper
    return type_check_decorator


@takes(int, str)
def f(a, b):
    print(f"Successful call with a={a} and b={b}")


if __name__ == '__main__':
    try:
        f(1, 2)
    except TypeError as e:
        print(f"TypeError: {e}")
    f(1, 'ab')
