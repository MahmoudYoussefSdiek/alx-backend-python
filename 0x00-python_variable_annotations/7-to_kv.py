#!/usr/bin/env python3
"""
This is a module that provides a to_kv function.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float, returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v.
    """
    return (k, v ** 2)
