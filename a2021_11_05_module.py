# Author: Gan Li
# Date: 11/5/21 5:45 下午
# Description: Decorator
import functools


def greeting(name):
    return "Hello " + name


def shout(func, name):
    return func(name).upper()


def debug(func):
    """Prints messages when entering and leaving the decorated function"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Entering", func.__name__)
        result = func(*args, **kwargs)
        print("Exiting", func.__name__)
        return result
    return wrapper
