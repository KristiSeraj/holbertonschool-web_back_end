#!/usr/bin/env python3
"""Strings To Redis"""
import redis
from typing import Union, Optional, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count methods"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Shows the call history"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input = f"{method.__qualname__}:inputs"
        output = f"{method.__qualname__}:outputs"

        self._redis.rpush(input, str(args))

        res = method(self, *args, **kwargs)

        self._redis.rpush(output, str(res))

        return res
    return wrapper


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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


def replay(method: Callable):
    """Display the history of call of a particular function"""
    method_name = method.__qualname__
    r = redis.Redis()

    inputs = r.lrange(f"{method.__qualname__}:inputs", 0, -1)
    outputs = r.lrange(f"{method.__qualname__}:outputs", 0, -1)

    print(f"{method_name} was called {int(r.get(method.__qualname__))} times:")

    for key, value in zip(*[inputs, outputs]):
        print(f"{method_name} (*{key.decode()}) -> {value.decode()}")
