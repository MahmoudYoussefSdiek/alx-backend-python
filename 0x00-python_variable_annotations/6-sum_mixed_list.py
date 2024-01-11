#!/usr/bin/env python3
"""
This is a module that provides a sum_mixed_list function.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list of integers and floats.
    """
    return sum(mxd_lst)
