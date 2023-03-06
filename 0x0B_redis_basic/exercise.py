#!/usr/bin/env python3
"""Strings To Redis"""
import redis
from typing import Union, Optional, Callable
import uuid


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[int, str], str]] = None):
        """Get the value of the key"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str):
        """Str format using get method"""
        return self.get(key, str)

    def get_int(self, key: str):
        """Int format using get method"""
        return self.get(key, int)
