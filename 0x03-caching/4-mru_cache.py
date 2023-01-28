#!/usr/bin/env python3
"""MRU Cache Module"""
import collections
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache Class"""
    def __init__(self):
        """Init method inheriting from base class"""
        super().__init__()
        self.deque = collections.deque()

    def put(self, key, item):
        """
        Assign to the dictionary cache_data the item for value key
        Removes the first element of dictionary
        if len of dictionary is bigger than max_items
        """
        if key and item:
            if key in self.cache_data:
                self.deque.remove(key)
            elif len(self.cache_data) == BaseCaching.MAX_ITEMS:
                mru = self.deque.pop()
                del self.cache_data[mru]
                print(f"DISCARD: {mru}")
            self.deque.appendleft(key)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value of key found in cache_data dictionary"""
        if key and self.cache_data.get(key):
            # self.deque.remove(key)
            # self.deque.appendleft(key)
            return self.cache_data.get(key)
        return None
