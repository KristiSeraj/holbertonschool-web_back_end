#!/usr/bin/env python3
"""TypeVar module"""
from typing import Union, Any, Mapping, TypeVar

T = TypeVar("T")


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Shows every type annotations for arguments"""
    if key in dct:
        return dct[key]
    else:
        return default
