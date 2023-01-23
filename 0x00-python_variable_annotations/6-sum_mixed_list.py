#!/usr/bin/env python3
"""Mixed list module"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Return sum of a list with int and floats"""
    return sum(mxd_list)
