#!/usr/bin/env python3
"""LRU CACHE"""
import collections
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache Class"""
    def __init__(self):
        """Init method inheriting from base class"""
        super().__init__()
        self.cache_data = collections.OrderedDict()

    def put(self, key, item):
        """
        Assign to the dictionary cache_data the item for value key
        Removes the first element of dictionary
        if len of dictionary is bigger than max_items
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                el = next(iter(self.cache_data))
                self.cache_data.pop(el)
                print(f"DISCARD: {el}")

    def get(self, key):
        """Retrieve the value of key found in cache_data dictionary"""
        if key and self.cache_data.get(key):
            return self.cache_data.get(key)
        return None
