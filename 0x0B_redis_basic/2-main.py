#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache
count_calls = __import__('exercise').count_calls

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))