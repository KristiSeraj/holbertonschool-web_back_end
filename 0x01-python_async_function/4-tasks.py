#!/usr/bin/env python3
"""Tasks module"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Same as wait_n function but task_wait_random is called"""
    valueList: List[float] = []
    all_values: List[float] = []
    for i in range(n):
        valueList.append(task_wait_random(max_delay))
    for task in asyncio.as_completed(valueList):
        res = await task
        all_values.append(res)
    return all_values
