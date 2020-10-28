#!/usr/bin/env python3
import functools
from datetime import datetime
from typing import Callable


def logger(log_file_path: str) -> Callable:
    with open(log_file_path, "w"):
        pass

    def logger_decorator(function: Callable) -> Callable:
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            with open(log_file_path, "a") as log_file:
                datetime_now = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
                result = function(*args, **kwargs)
                print(
                    f"{datetime_now} {wrapper.__name__} "
                    f"({args}) ({kwargs}) {result}",
                    file=log_file
                )
                return result
        return wrapper
    return logger_decorator


@logger("my_log.txt")
def f(n):
    if n != 0:
        return f(n - 1)


if __name__ == '__main__':
    f(5)
