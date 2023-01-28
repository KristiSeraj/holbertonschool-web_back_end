#!/usr/bin/env python3
"""MRU Cache Module"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache Class"""
    def __init__(self):
        """Init method inheriting from base class"""
        super().__init__()
        self.deque = deque()

    def add_el(self, element):
        """Adds element to the last index of list"""
        length_deque = len(self.deque)
        if self.deque[length_deque - 1] != element:
            self.deque.remove(element)
            self.deque.append(element)

    def put(self, key, item):
        """
        Assign to the dictionary cache_data the item for value key
        Removes the first element of dictionary
        if len of dictionary is bigger than max_items
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.deque:
                    mru = self.deque.pop()
                    del self.cache_data[mru]
                    print(f"DISCARD: {mru}")
        if key not in self.deque:
            self.deque.append(key)
        else:
            self.add_el(key)

    def get(self, key):
        """Retrieve the value of key found in cache_data dictionary"""
        el = self.cache_data.get(key, None)
        if el is not None:
            self.add_el(key)
        return el
