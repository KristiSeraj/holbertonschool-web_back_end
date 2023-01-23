#!/usr/bin/env python3
"""Iterable module"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Length of a list"""
    return [(i, len(i)) for i in lst]
