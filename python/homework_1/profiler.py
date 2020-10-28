#!/usr/bin/env python3
import time
from typing import Callable


def profiler(function: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, "__calls"):
            setattr(wrapper, "__calls", 0)
            start_time = time.time()
            result = function(*args, **kwargs)
            end_time = time.time()
            setattr(wrapper, "last_time_taken", end_time - start_time)
            setattr(wrapper, "calls", getattr(wrapper, "__calls"))
            delattr(wrapper, "__calls")
            return result
        else:
            calls = getattr(wrapper, "__calls")
            setattr(wrapper, "__calls", calls + 1)
            return function(*args, **kwargs)
    return wrapper


@profiler
def f(n):
    if n != 0:
        f(n - 1)


if __name__ == '__main__':
    f(5)
    f(5)
    print(f"number of recursive calls: {f.calls}")
    print(f"execution time: {f.last_time_taken}")
