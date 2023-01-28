#!/usr/bin/env python3
"""FIFO CACHE"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache Class"""
    def put(self, key, item):
        """
        Assign to the dictionary cache_data the item for value key
        Removes the first element of dictionary
        if len of dictionary is bigger than max_items
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_el = next(iter(self.cache_data))
            print(f"DISCARD: {first_el}")
            self.cache_data.pop(first_el)

    def get(self, key):
        """Retrieve the value of key found in cache_data dictionary"""
        if key and self.cache_data.get(key):
            return self.cache_data.get(key)
        return None
