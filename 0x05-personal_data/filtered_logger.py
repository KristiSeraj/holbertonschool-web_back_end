#!/usr/bin/env python3
"""Regex-ing module"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Filter datum that returns the log message obfuscated"""
    for el in fields:
        message = re.sub(fr'{el}=[\w\d\/]+{separator}',
                         fr'{el}={redaction}{separator}',
                         message)
    return message
