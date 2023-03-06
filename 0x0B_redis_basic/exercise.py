#!/usr/bin/env python3
"""Strings To Redis"""
import redis
from typing import Any
import uuid


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """Generates a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
