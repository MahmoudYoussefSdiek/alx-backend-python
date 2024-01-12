#!/usr/bin/env python3
"""
This is a module that provides a safely_get_value function.
"""
from typing import Mapping, TypeVar, Any, Union, Optional

# Define a generic type variable
T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Optional[T] = None) -> Union[T, None]:
    """
    Safely retrieves the value associated with the key in the dictionary.
    If the key is not present, returns the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
