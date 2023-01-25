#!/usr/bin/env python3
"""Async comprehensions module"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Collect 10 random numbers using async comprehensions
    with async generator and returns the 10 random numbers
    """
    result = [i async for i in async_generator()]
    return result
