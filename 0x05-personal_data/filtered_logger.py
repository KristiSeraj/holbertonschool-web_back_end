#!/usr/bin/env python3
"""Regex-ing module"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Filter datum that returns the log message obfuscated"""
    message = re.sub(fr'{fields[0]}=\w+{separator}', fr'{fields[0]}={redaction}{separator}', message)
    return re.sub(fr'{fields[1]}=\b\d+\/\d+\/\d+{separator}', fr'{fields[1]}={redaction}{separator}', message)
