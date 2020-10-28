#!/usr/bin/env python3
from collections import OrderedDict
from typing import Callable


def cached(max_size: int = None) -> Callable:
    cached_result = OrderedDict()

    def cache_decorator(function: Callable) -> Callable:
        def wrapper(*args):
            if len(args) == 0:
                args = function.__defaults__
            if args in cached_result:
                print(f"found {args} in cache!")
                return cached_result[args]
            print(f"there are no {args} in cache!")
            if max_size is not None and len(cached_result) == max_size:
                cached_result.popitem(last=True)
            cached_result[args] = function(*args)
            return cached_result[args]
        return wrapper
    return cache_decorator


@cached(1)
def f(n=1):
    pass


if __name__ == "__main__":
    f(1)
    f()
    f(2)
    f(1)
