#!/usr/bin/env python3
"""Measure runtime module"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehesion four times in parallel using asyncio.gather
    and measure the total runtime and return it
    """
    start_time = time.time()
    await asyncio.gather(
        *[async_comprehension(),
          async_comprehension(),
          async_comprehension(),
          async_comprehension()]
    )
    end_time = time.time()
    elapse_time = end_time - start_time
    return elapse_time
