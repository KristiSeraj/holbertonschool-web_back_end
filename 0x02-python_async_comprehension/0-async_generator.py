#!/usr/bin/env python3
"""Async generator module"""
import random
import asyncio


async def async_generator():
    """
    Coroutine that loops 10 times and waits 1 second
    then yield a random number between 0 and 10 using random module
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
