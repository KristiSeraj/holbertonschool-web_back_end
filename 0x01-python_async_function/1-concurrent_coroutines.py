#!/usr/bin/env python3
"""Async module"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Imports wait_random from the basic async file and calles wait_n
    that takes 2 int arguments. Spawns wait_random, n times with max_delay
    Return: list of all delays (float values) in ascending order
    """
    valueList: List[float] = []
    all_values: List[float] = []
    for i in range(n):
        valueList.append(wait_random(max_delay))
    for task in asyncio.as_completed(valueList):
        res = await task
        all_values.append(res)
    return all_values
