#!/usr/bin/env python3
"""LIFO CACHE"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache Class"""
    def __init__(self):
        """Init method inheriting from base class"""
        super().__init__()
        self.last = ''

    def put(self, key, item):
        """
        Assign to the dictionary cache_data the item for value key
        Removes the first element of dictionary
        if len of dictionary is bigger than max_items
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print(f"DISCARD: {self.last}")
                self.cache_data.pop(self.last)
            self.last = key

    def get(self, key):
        """Retrieve the value of key found in cache_data dictionary"""
        if key and self.cache_data.get(key):
            return self.cache_data.get(key)
        return None
