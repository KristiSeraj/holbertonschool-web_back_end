#!/usr/bin/env python3
"""Functions module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float with multiplier"""
    def func(n: float) -> float:
        return n * multiplier
    return func
