#!/usr/bin/env python3
"""First element of a sequence"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns any type or none"""
    if lst:
        return lst[0]
    else:
        return None
