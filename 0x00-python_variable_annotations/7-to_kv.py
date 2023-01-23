#!/usr/bin/env python3
"""Complex types module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple with string and int/float"""
    v = v ** 2
    return (k, v)
