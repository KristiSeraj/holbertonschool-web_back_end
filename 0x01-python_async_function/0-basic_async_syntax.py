#!/usr/bin/env python3
"""Async module"""
import asyncio
import random


async def wait_random(max_delay: int =10) -> float:
    """Asynchronous coroutine that takes in an integer and waits
    for a random delay between 0 and max_delay"""
    random_n = random.uniform(0, max_delay)
    await asyncio.sleep(random_n)
    return random_n
